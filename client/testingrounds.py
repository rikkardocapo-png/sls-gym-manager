
import mysql.connector as mysql
import tkinter.messagebox as message



def findid1():

    try:
        connection = mysql.connect(host="localhost", user="sls-modifyer", database="gym manager data", port=3306)
        cursor = connection.cursor()
        cursor.execute(f"SELECT AccID from users ORDER BY AccID DESC")
        cursor.execute("commite")
        biggest_id = int(cursor.fetchone())
        print("biggest id (success) "+ str(biggest_id))
    except:
        biggest_id = 0
        print("biggest id (fail) " + str(biggest_id))
    return biggest_id + 1

import mysql.connector as mysql
from mysql.connector import Error

def login(e_user, e_pass):
   global loggeduser, AccID
   username = e_user
   password = e_pass
   if e_user == "" or e_pass == "":
       message.showinfo("Get Status", "Some fields are empty")
   else:
       try:
           connection = mysql.connect(host="localhost", user="sls-modifyer", database="gym manager data",port=3306)
           cursor = connection.cursor()
           cursor.execute(f"Select AccID from Users WHERE Email = {username} AND Password = {password}")
           cursor.execute("commit")
           ACCID = cursor.fetchone[0]
           loggeduser = ACCID
           OpenHome()



