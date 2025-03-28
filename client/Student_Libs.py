


#Importing libraries

import mysql.connector as mysql
import tkinter.messagebox as message
import urllib.parse
import subprocess
import platform
from tkinter import filedialog
from datetime import timedelta
from datetime import datetime
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import sys

def load_env():
    # This function is needed to load the .env file containing the encrypted credentials for connection. It is defined here as it has to be called as soon as possible. This is done so 12 lines below this.
    if getattr(sys, 'frozen', False):

        base_path = sys._MEIPASS
        env_path = os.path.join(base_path, 'Resources', '.env')
    else:
        env_path = os.path.abspath("../../AppPacking/CLIENTAPP/.env")
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"Filenotfound")
    load_dotenv(dotenv_path=env_path)

#Connection variables
load_env()
Ehost = os.getenv('DB_HOST')
Euser = os.getenv('DB_USER')
Epsw = os.getenv('DB_PASSWORD')
Eatabase = os.getenv('DB_DATABASE')
Eport = os.getenv('DB_PORT')



host = None
user = None
psw = None
atabase = None
port = ""
cursor=None
connection=None



#Server connection subroutines

def initialize_connection():
    global cursor
    global connection
    global host, user, database, port, psw
    # Here the app tries to connect to the server and set up a cursor. This cursor is kept for the length of the section to limit lag and resource usage
    port=int(port)
    try:
        connection = mysql.connect(host=host, user=user, database=database, password=psw, port=port, connection_timeout=300)
        cursor = connection.cursor()
    except Exception as e:
        

        return None

def close_connection():
    global connection
    global cursor
    # Here the app closes the connection by force closing connection and cursor. This is the CORRECT way to close the app however if the app is forcequit it wont trigger. Anyways any connection times out after 8h
    if connection:
        connection.close()

    if cursor:
        cursor.close()

def connect(query,params):
    global cursor
    global connection
    # This is the backbone of the whole backend of the app. This function takes the query and the parametres of the query separately (to prevent SQL injection attacks) before executing and returning values (if necessary)

    try:
        if not connection.is_connected():
            close_connection()
            initialize_connection()
    except Exception as e:
        message.showinfo("Connection failure", f"Error:{e}")
        return None

    try:
        cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
        cursor.execute(query,params)
        if query.strip().upper().startswith(("INSERT", "DELETE", "UPDATE")):
            connection.commit()
        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchone()
            return result

    except Exception as e:
        message.showinfo("SQl failure", f"Error:{e}")
        return None



#Checking/status functions

def isweekend(date_str):
    # This function checks if a date is a weekend day, used for the timetable
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_week = date_obj.weekday()
    if day_of_week < 5:
        return True
    else:
        return False

def checkpresent(username):
    # This function prevents a user from utlilizing the same mail twice for making two accounts
   try:
       record = connect("SELECT Email FROM Users WHERE Email = %s", (username,))
       return record

   except mysql.Error:
       return None

def findid():
    # This function makes an accountID primary key dynamically by adding one to the biggest ID in the server
    try:
        result = connect("SELECT AccID FROM Users ORDER BY AccID DESC LIMIT 1", ())
        if result and result[0] is not None:
            biggest_id = int(result[0])
        else:
            biggest_id = 0
    except:
        pass

    return biggest_id + 1

def IDtoName(ACCID):
    # This function gets the name of the owner of this account
    Name = connect("SELECT Name, Surname FROM Users WHERE AccID = %s", (ACCID,))[0]
    Surname = connect("SELECT Name, Surname FROM Users WHERE AccID = %s", (ACCID,))[1]

    return Name,Surname

def getday(adder):
    # This function translated dynamically the coordinate system of the timetable to actual days
    today = datetime.today()
    future_date = today + timedelta(days=adder)
    return future_date.date()

def getTTstatus(i,o,AccID):
    # This function gets the status of the periods on both fullness and colour that the button should be
    result = connect("SELECT COUNT(*) AS count_entries FROM Timetable WHERE Period = %s AND Date = %s", (o, getday(i)))[0]

    present = connect("SELECT * from Timetable WHERE Period = %s AND Date = %s AND AccID = %s", (o, getday(i), AccID))


    if present == None:
        if result == 20:
            style = "Red.TButton"
        elif result >= 10 and result < 20:
            style = "Yellow.TButton"
        elif result >=0 and result < 10 :
            style = "Green.TButton"
        else:
            pass
    else:
        style = "Purple.TButton"

    result = f"{result}/20"

    return result,style

def MedStatus(AccID):
    # This function retrieves the account's certificate's status and expiration time along with what colour the displayed label should be
    result=connect("SELECT Expiry FROM Certificates WHERE MedID = %s",(AccID,))
    if result == None:
        return "Not submitted","red",False
    elif connect("SELECT Approved FROM Certificates WHERE MedID = %s",(AccID,))[0] == 0:
        return "Not yet approved", "lightblue", False

    else:
        result=result[0]
        if getday(0) <= result and result <= getday(14):
            return f"Expires in {(result-getday(0)).days} days", "yellow",True

        elif result < getday(0):
            return "Expired", "red",False

        else:
            return "Submitted", "green",True

def IndStatus(AccID):
    # This function does the same as the above but for the induction day wich is either done or not done
    if connect("SELECT Induction FROM Users WHERE AccID = %s",(AccID,))[0] == 0:
        return "Not completed","red",False
    else:
        return "Completed","green",True

def checkteacher(AccID):
    # This function checks to see if the account is teacher enabled and therefore can access teacher-only slots
    query = "SELECT Teacher FROM Users WHERE AccID = %s"
    params = (AccID,)
    result = connect(query,params)[0]

    if result == 0:
        return False
    elif result == 1:
        return True



#Account functions

def login(e_user, e_pass,open_home_callback):
    global loggeduser, AccID
    # This function is required to log in. What it does is it compares credentials with the ones saved on the server and sees if they are valid. If yes it callbacks the homepage and opens it with the appropriate account
    username = e_user
    password = e_pass
    if username == "" or password == "":
        message.showinfo("Get Status", "Some fields are empty")
    else:
        try:
            ACCID = connect("SELECT AccID FROM Users WHERE Email = %s AND Password = %s", (username, password))
            if ACCID == None:
                message.showinfo("Login status", "Invalid username or password")
            else:
                ACCID = int(ACCID[0])

                loggeduser = ACCID
                open_home_callback(loggeduser)


        except mysql.Error as e:
            message.showinfo("Login status", f"SQL error: {e}")

def signup(username, password, name, sur, logincallback):
    # This function makes a user account if valid credentials are given and opens the login page if the signup is successful
    if username == "" or password == "":
        message.showinfo("Insert status", "Some fields are empty")
    elif checkpresent(username):
        message.showinfo("Insert status", "E-mail taken, try logging in")
    elif not("@" in username and "." in username.split("@")[-1]):
        message.showinfo("Insert status", "Invalid e-mail ")

    else:

       connect("INSERT INTO Users VALUES (%s, %s, %s, %s, %s, FALSE, FALSE)", (findid(), name, sur, username, password))
       message.showinfo("Insert status", "Sign-up successful")
       logincallback()



#App/Miscellaneous functions

def TTBTN_press(i, o, AccID, button):
    if not checkteacher(AccID) and o >= 3:
    # This function controls the main functionality of the app: booking periods. It does a host of checks to see if the account actually has permission to book the specific period
        message.showinfo("Teachercheck - Failed", "Error - Non teacher account")
        return

    elif not MedStatus(AccID)[2]:
        message.showinfo("Medcheck - Failed", "Error - Certificate invalid")
        return

    elif not IndStatus(AccID)[2]:
        message.showinfo("Indcheck - Failed", "Error - Induction not complete")
        return

    elif connect("SELECT COUNT(*) AS count_entries FROM Timetable WHERE Period = %s AND Date = %s", (o, getday(i)))[0] == 20:
        message.showinfo("Fullcheck - Failed", "Error - period full")
        return

    if connect("SELECT * FROM Timetable WHERE AccID = %s AND Period = %s AND Date = %s",(AccID, o, getday(i))) is None:
        connect("INSERT INTO Timetable VALUES (%s, %s, %s, 0)",(getday(i), o, AccID))
    else:
        connect("DELETE FROM Timetable WHERE AccID = %s AND Period = %s AND Date = %s",(AccID, o, getday(i)))

    new_text,new_style = getTTstatus(i, o, AccID)
    button.configure(style=new_style, text=new_text)

def sendemail(sendto, AccID, ind):
    name = IDtoName(AccID)[0]
    surname = IDtoName(AccID)[1]
    # This function opens up the system mailing app to contact either the gym manager directly or tech support (me in this case)
    if ind is None:
        subject = "Gym Manager Automated Support Request"
        body = f"{name} {surname} has sent a message:\n\n*Include message here*"
    else:
        subject = "Gym Manager Automated Induction Request"
        body = f"{name} {surname} wants to organize an Induction Day\n\n*Include message here*"

    subject_enc = urllib.parse.quote(subject)
    body_enc = urllib.parse.quote(body)

    mail = f"mailto:{sendto}?subject={subject_enc}&body={body_enc}"
    system_platform = platform.system()
    try:
        if system_platform == "Windows":
            subprocess.run(["open", "-a", "Mail", mail], check=True)
        elif system_platform == "Darwin": 
            subprocess.run(["open", "-a", "Mail", mail], check=True)
        else:
            message.showinfo("System error","This platform is not supported.")
    except subprocess.CalledProcessError as e:
        message.showinfo("System error",f"Failed to open email client: {e}")

def valiDate(date_str):
    # This function validates the date hence the funny name. It is used to see if the user inputted a valid date of expiry for the certificate
    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        today = datetime.now()
        if date_obj <= today:
            return False

        return True
    except ValueError:
        return False





#File functions

def select_file(button):
    global filepath
    # This function opens the filedialog selector integrated with the OS to select a file. It also limits selection to pdf files
    file_path = filedialog.askopenfilename(title="Select an Image File",filetypes=[("PDF files", "*.pdf")])

    if file_path and file_path.endswith('.pdf'):
        filepath = file_path
        file_name = os.path.basename(file_path)
        button.configure(text=file_name)
    else:
        message.showinfo("Error","Be sure to select a valid PDF file")

def upload_file(entry,AccID):
    global filepath
    # This function proceeds to actually add the certificate file to the server but it does so only after a date, presence, validity and size check are passed.
    date = entry.get()

    if not valiDate(date):
        message.showinfo("Upload failure", "No valid date (dd/mm/YYYY)")

    if not filepath:
        message.showinfo("Upload Failure", "No file selected.")

    if not os.path.isfile(filepath):
        message.showinfo("Upload Failure", "File path is not valid.")


    else:
        date_obj = datetime.strptime(date, '%d/%m/%Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        if not connect("SELECT * FROM Certificates WHERE MedID = %s",(AccID,)):
            try:
                with open(filepath, 'rb') as file:
                    binary_data = file.read()
                bytes = len(binary_data)
                if bytes <= 2000000:
                    query = "INSERT INTO Certificates (MedID, Image, Expiry, Approved) VALUES (%s, %s, %s, False)"
                    params = (AccID, binary_data, formatted_date)
                    connect(query,params)
                    message.showinfo("Upload success", "Uploaded successfully")
                else:
                    message.showinfo("Upload faliure", "File too big (>2mb)")
            except Exception as e:
                message.showinfo("Upload failure", f"Error:{e}")
        else:
            try:
                with open(filepath, 'rb') as file:
                    binary_data = file.read()
                bytes = len(binary_data)
                if bytes <= 2000000:
                    query = "UPDATE Certificates SET Image = %s, Expiry = %s, Approved = False WHERE MedID = %s"
                    params = (binary_data, formatted_date, AccID)
                    connect(query,params)
                    message.showinfo("Upload success", "Uploaded successfully")
                else:
                    message.showinfo("Upload faliure", "File too big (>2mb)")
            except Exception as e:
                message.showinfo("Upload failure", f"Error:{e}")

#Security functions

def load_key():
    # This function loads the key to decrypt the rest of the credentials
    load_dotenv()
    key_file = os.getenv('DB_K')
    return key_file

def load_creds():
    global host, user, psw, database, port
    # This function loads the credentials with the key retrieved above
    key = load_key()
    cipher = Fernet(key)

    load_dotenv()
    encrypted_host = os.getenv('DB_HOST')
    encrypted_user = os.getenv('DB_USER')
    encrypted_password = os.getenv('DB_PASSWORD')
    encrypted_database = os.getenv('DB_DATABASE')
    encrypted_port = os.getenv('DB_PORT')

    host = cipher.decrypt(encrypted_host.encode()).decode()
    user = cipher.decrypt(encrypted_user.encode()).decode()
    psw = cipher.decrypt(encrypted_password.encode()).decode()
    database = cipher.decrypt(encrypted_database.encode()).decode()
    port = cipher.decrypt(encrypted_port.encode()).decode()

