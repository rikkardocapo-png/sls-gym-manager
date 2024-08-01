import mysql.connector as mysql
import tkinter.messagebox as message


def checkpresent(username):
   connection = mysql.connect(host="localhost",user="sls-modifyer",database="gym manager data",port=3306)

   try:
       cursor = connection.cursor()
       cursor.execute(f"SELECT Email FROM users WHERE Email = '{username}'")
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
        connection = mysql.connect(host="localhost",user="sls-modifyer",database="gym manager data",port=3306)
        cursor = connection.cursor()
        cursor.execute("SELECT AccID FROM users ORDER BY AccID DESC LIMIT 1")
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
           connection = mysql.connect(host="localhost", user="sls-modifyer", database="gym manager data",port=3306)
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
            connection = mysql.connect(host="localhost", user="sls-modifyer", database="gym manager data", port=3306)
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

def signup(username, password, name, sur):

    if username == "" or password == "":
       message.showinfo("Insert status", "Some fields are empty")
    elif checkpresent(username):
       message.showinfo("Insert status", "E-mail taken, try logging in")

    else:
       con = mysql.connect(host="localhost", user="sls-modifyer", database="gym manager data", port=3306)
       cursor = con.cursor()
       cursor.execute(f"insert into users values('{findid()}','{name}','{sur}','{username}','{password}',FALSE)")
       cursor.execute("commit")
       cursor.close()
       con.close()

def IDtoName(ACCID):
    connection = mysql.connect(host="localhost", user="sls-modifyer", database="gym manager data", port=3306)
    cursor = connection.cursor()
    cursor.execute(f"SELECT Name FROM users WHERE AccID = '{ACCID}'")
    result = cursor.fetchone()
    result = result[0]
    cursor.close()
    connection.close()
    return result

