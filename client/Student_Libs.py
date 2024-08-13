import mysql.connector as mysql
import tkinter.messagebox as message
from datetime import datetime, timedelta

def checkpresent(username):
   connection = mysql.connect(host="localhost",user="sls-modifyer",database="IA User-data",port=8889)

   try:
       cursor = connection.cursor()
       cursor.execute(f"SELECT Email FROM Users WHERE Email = '{username}'")
       record = cursor.fetchone()

       return record

   except mysql.Error:
       print("No match found")
       return None

   finally:
       if connection.is_connected():
           cursor.close()
           connection.close()

def findid():
    try:
        connection = mysql.connect(host="localhost",user="sls-modifyer",database="IA User-data",port=8889)
        cursor = connection.cursor()
        cursor.execute("SELECT AccID FROM Users ORDER BY AccID DESC LIMIT 1")
        result = cursor.fetchone()
        if result and result[0] is not None:
            biggest_id = int(result[0])
        else:
            biggest_id = 0
    except:
        print("error during find check")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return biggest_id + 1

"""def login(e_user, e_pass):
   global loggeduser, AccID
   username = e_user
   password = e_pass
   if e_user == "" or e_pass == "":
       message.showinfo("Get Status", "Some fields are empty")
   else:
       try:
           connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data",port=8889)
           cursor = connection.cursor()
           cursor.execute(f"Select AccID from Users WHERE Email = '{username}' AND Password = '{password}'")
           cursor.execute("commit")
           ACCID = cursor.fetchall()

           if ACCID != None:
               loggeduser = ACCID
               OpenHome()



       except mysql.Error as e:
           message.showinfo("Login status", f"sql error {e}")
       finally:
           cursor.close()
           connection.close()"""

def login(e_user, e_pass,open_home_callback):
    global loggeduser, AccID
    username = e_user
    password = e_pass
    if username == "" or password == "":
        message.showinfo("Get Status", "Some fields are empty")
    else:
        try:
            connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
            cursor = connection.cursor()
            cursor.execute(f"SELECT AccID FROM Users WHERE Email = '{username}' AND Password = '{password}'")
            ACCID = cursor.fetchone()
            if ACCID == None:
                message.showinfo("Login status", "Invalid username or password")
            else:
                ACCID = int(ACCID[0])

                loggeduser = ACCID
                print(ACCID)
                open_home_callback(loggeduser)


        except mysql.Error as e:
            message.showinfo("Login status", f"SQL error: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()

def signup(username, password, name, sur, logincallback):

    if username == "" or password == "":
       message.showinfo("Insert status", "Some fields are empty")
    elif checkpresent(username):
       message.showinfo("Insert status", "E-mail taken, try logging in")

    else:
       con = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
       cursor = con.cursor()
       cursor.execute(f"insert into Users values('{findid()}','{name}','{sur}','{username}','{password}',FALSE)")
       cursor.execute("commit")
       cursor.close()
       con.close()
       message.showinfo("Insert status", "Sign-up successful")
       logincallback()

def IDtoName(ACCID):
    connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
    cursor = connection.cursor()
    cursor.execute(f"SELECT Name FROM Users WHERE AccID = '{ACCID}'")
    result = cursor.fetchone()
    result = result[0]
    cursor.close()
    connection.close()
    return result

def getday(adder):
    today = datetime.today()
    future_date = today + timedelta(days=adder)
    return future_date.date()

def getTTstatus(i,o,AccID):
    connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
    cursor = connection.cursor()
    cursor.execute(f"SELECT COUNT(*) AS count_entries FROM Timetable WHERE Period = '{o}' AND Date = '{getday(i)}'")
    result = cursor.fetchone()[0]
    cursor.execute(f"SELECT * from Timetable WHERE Period = '{o}' AND Date = '{getday(i)}' AND AccID = '{AccID}' ")
    present = cursor.fetchone()
    cursor.close()
    connection.close()

    if present == None:
        if result == 20:
            colour = "red"
        elif result >= 10 and result < 20:
            colour = "yellow"
        elif result >=0 and result < 10 :
            colour = "green"
        else:
            print("warning - exceeded max capacity")
    else:
        colour = "#7B68EE"

    result = f"{result}/20"

    return result,colour

def closewindows():
    global SU_window, LG_window, H_window, B_window
    try:
        H_window.destroy()
    except:
        pass
    try:
        B_window.destroy()
    except:
        pass
    try:
        LG_window.destroy()
    except:
        pass
    try:
        SU_window.destroy()
    except:
        pass

def MedStatus(AccID):
    connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
    cursor = connection.cursor()
    cursor.execute(f"SELECT Expiry FROM Certificates WHERE MedID = '{AccID}'")
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result == None:
        return "Not submitted","red"
    else:
        result=result[0]
        if getday(0) <= result <= getday(14):
            return f"Expires in {(result-getday(0)).days} days", "yellow"

        elif result < getday(0):
            return "Expired", "red"

        else:
            return "Submitted", "green"

def IndStatus(AccID):
    connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
    cursor = connection.cursor()
    cursor.execute(f"SELECT Induction FROM Users WHERE AccID = '{AccID}'")
    result = cursor.fetchone()[0]
    cursor.close()
    connection.close()

    if result == 0:
        return "Not completed","red"
    else:
        return "Completed","green"

"""def TTBTN_press(i,o,AccID,button):

    if checkteacher(AccID) == False and o >= 3:
        message.showinfo("Teachercheck - Failed", "Error - non teacher accounts cannot access such periods")
    else:


        connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM Timetable WHERE AccID = '{AccID}' AND Period = '{o}' AND Date = '{getday(i)}'")
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result == None:
            connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO Timetable VALUES ('{getday(i)}','{o}','{AccID}',0)")
            connection.commit()
            print("called-none")
            cursor.close()
            connection.close()
        else:
            connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM Timetable WHERE AccID = '{AccID}' AND Period = '{o}' AND Date = '{getday(i)}'")
            connection.commit()
            print("called-present")
            cursor.close()
            connection.close()

        new_text, new_bg = Funcs.getTTstatus(i, o, AccID)
        button.config(text=new_text, bg=new_bg)"""

def TTBTN_press(i, o, AccID, button):
    if not checkteacher(AccID) and o >= 4:
        message.showinfo("Teachercheck - Failed", "Error - non teacher accounts cannot access such periods")
        return

    connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Timetable WHERE AccID = '{AccID}' AND Period = '{o}' AND Date = '{getday(i)}'")
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result is None:
        connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO Timetable VALUES ('{getday(i)}', '{o}', '{AccID}', 0)")
        connection.commit()
        cursor.close()
        connection.close()
        print("called-none")
    else:
        connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM Timetable WHERE AccID = '{AccID}' AND Period = '{o}' AND Date = '{getday(i)}'")
        connection.commit()
        cursor.close()
        connection.close()
        print("called-present")


    new_text, new_bg = getTTstatus(i, o, AccID)
    button.configure(text=new_text, bg=new_bg,anchor="center", justify="center")


def checkteacher(AccID):
    connection = mysql.connect(host="localhost", user="sls-modifyer", database="IA User-data", port=8889)
    cursor = connection.cursor()
    cursor.execute(f"SELECT Teacher FROM Users WHERE AccID = '{AccID}'")
    result = cursor.fetchone()[0]
    cursor.close()
    connection.close()

    if result == 0:
        return False
    elif result == 1:
        return True