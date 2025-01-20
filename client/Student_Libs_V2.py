import mysql.connector as mysql
import tkinter.messagebox as message



import urllib.parse
import subprocess
import platform
import os
from tkinter import filedialog
from datetime import datetime, timedelta

from Serverapp.test import password

#Connection variables
"""
host="localhost"
user="sls-modifyer"
database="IA User-data"
port=8889"""

host="sql.slsprojects.it"
user="slsproje37171"
database="slsproje37171"
port=3306
psw="REDACTED"

#Functional subroutines

def isweekend(date_str):

    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_week = date_obj.weekday()
    if day_of_week < 5:
        return True
    else:
        return False

def checkpresent(username):

   try:
       record = connect("SELECT Email FROM Users WHERE Email = %s", (username,))
       return record

   except mysql.Error:
       return None

def findid():
    try:

        result = connect("SELECT AccID FROM Users ORDER BY AccID DESC LIMIT 1", ())
        if result and result[0] is not None:
            biggest_id = int(result[0])
        else:
            biggest_id = 0
    except:
        print("error during find check")

    return biggest_id + 1

def login(e_user, e_pass,open_home_callback):
    global loggeduser, AccID
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

    if username == "" or password == "":
        message.showinfo("Insert status", "Some fields are empty")
    elif checkpresent(username):
        message.showinfo("Insert status", "E-mail taken, try logging in")
    elif not("@" in username and "." in username.split("@")[-1]):
        message.showinfo("Insert status", "Invalid e-mail ")

    else:

       connect("INSERT INTO Users VALUES (%s, %s, %s, %s, %s, FALSE)", (findid(), name, sur, username, password))
       message.showinfo("Insert status", "Sign-up successful")
       logincallback()

def IDtoName(ACCID):

    Name = connect("SELECT Name, Surname FROM Users WHERE AccID = %s", (ACCID,))[0]
    Surname = connect("SELECT Name, Surname FROM Users WHERE AccID = %s", (ACCID,))[1]

    return Name,Surname

def getday(adder):
    today = datetime.today()
    future_date = today + timedelta(days=adder)
    return future_date.date()

def getTTstatus(i,o,AccID):

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
            print("warning - exceeded max capacity")
    else:
        style = "Purple.TButton"

    result = f"{result}/20"

    return result,style

def MedStatus(AccID):
    result=connect("SELECT Expiry FROM Certificates WHERE MedID = %s",(AccID,))

    if result == None:
        return "Not submitted","red",True
    elif connect("SELECT Approved FROM Certificates WHERE MedID = %s",(AccID,))[0] == 0:
        return "Not yet approved", "lightblue", False

    else:
        result=result[0]
        if getday(0) <= result <= getday(14):
            return f"Expires in {(result-getday(0)).days} days", "yellow",True

        elif result < getday(0):
            return "Expired", "red",False

        else:
            return "Submitted", "green",True

def IndStatus(AccID):

    if connect("SELECT Induction FROM Users WHERE AccID = %s",(AccID,))[0] == 0:
        return "Not completed","red",False
    else:
        return "Completed","green",True

def TTBTN_press(i, o, AccID, button):
    if not checkteacher(AccID) and o >= 3:
        print(checkteacher(AccID))
        message.showinfo("Teachercheck - Failed", "Error - Non teacher account")
        return

    if not MedStatus(AccID)[2]:
        message.showinfo("Medcheck - Failed", "Error - Certificate invalid")
        return

    if not IndStatus(AccID)[2]:
        message.showinfo("Indcheck - Failed", "Error - Induction not complete")
        return

    if connect("SELECT COUNT(*) AS count_entries FROM Timetable WHERE Period = %s AND Date = %s", (o, getday(i)))[0] == 20:
        message.showinfo("Fullcheck - Failed", "Error - period full")
        return

    if connect("SELECT * FROM Timetable WHERE AccID = %s AND Period = %s AND Date = %s",(AccID, o, getday(i))) is None:
        connect("INSERT INTO Timetable VALUES (%s, %s, %s, 0)",(getday(i), o, AccID))
    else:
        connect("DELETE FROM Timetable WHERE AccID = %s AND Period = %s AND Date = %s",(AccID, o, getday(i)))

    new_text,new_style = getTTstatus(i, o, AccID)
    button.configure(style=new_style, text=new_text)

def checkteacher(AccID):
    query = "SELECT Teacher FROM Users WHERE AccID = %s"
    params = (AccID,)
    result = connect(query,params)[0]

    if result == 0:
        return False
    elif result == 1:
        return True

def sendemail(sendto, AccID, ind):
    name = IDtoName(AccID)[0]
    surname = IDtoName(AccID)[1]

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
        if system_platform == "Windows":    # Windows
            subprocess.run(['start', mail], shell=True, check=True)
        elif system_platform == "Darwin":  # macOS
            subprocess.run(['open', mail], check=True)
        else:
            message.showinfo("System error","This platform is not supported.")
    except subprocess.CalledProcessError as e:
        message.showinfo("System error",f"Failed to open email client: {e}")

def select_file(button):
    global filepath
    file_path = filedialog.askopenfilename(title="Select an Image File",filetypes=[("PDF files", "*.pdf")])

    if file_path and file_path.endswith('.pdf'):
        filepath = file_path
        file_name = os.path.basename(file_path)
        button.configure(text=file_name)
    else:
        message.showinfo("Error","Be sure to select a valid PDF file")

def valiDate(date_str):

    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except:
        return False

def upload_file(entry,AccID):
    global filepath
    date = entry.get()
    date_obj = datetime.strptime(date, '%d/%m/%Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')

    if not valiDate(date):
        message.showinfo("Upload failure", "No valid date (dd/mm/yyyy)")

    if not filepath:
        message.showinfo("Upload Failure", "No file selected.")

    if not os.path.isfile(filepath):
        message.showinfo("Upload Failure", "File path is not valid.")


    else:
        if not connect("SELECT * FROM Certificates WHERE MedID = %s",(AccID,)):
            try:
                with open(filepath, 'rb') as file:
                    binary_data = file.read()

                query = "INSERT INTO Certificates (MedID, Image, Expiry, Approved) VALUES (%s, %s, %s, False)"
                params = (AccID, binary_data, formatted_date)
                connect(query,params)
                message.showinfo("Upload success", "Uploaded successfully")
            except Exception as e:
                message.showinfo("Upload failure", f"Error:{e}")
        else:
            try:
                with open(filepath, 'rb') as file:
                    binary_data = file.read()

                query = "UPDATE Certificates SET Image = %s, Expiry = %s, Approved = False WHERE MedID = %s"
                params = (binary_data, formatted_date, AccID)
                connect(query,params)
                message.showinfo("Upload success", "Uploaded successfully")
            except Exception as e:
                message.showinfo("Upload failure", f"Error:{e}")

def connect(query,params):

    try:
        connection = mysql.connect(host=host, user=user, database=database, password=psw)
        cursor = connection.cursor()
        cursor.execute(query,params)

        if query.strip().upper().startswith(("INSERT", "DELETE", "UPDATE")):
            connection.commit()
        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchone()
            return result

    except Exception as e:
        message.showinfo("Connect failure", f"Error:{e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def refresh(root,procedure):

    root.destroy()
    procedure()


