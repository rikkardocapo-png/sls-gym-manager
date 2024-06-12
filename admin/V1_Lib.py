import schedule
import datetime
import mysql.connector as mysql

def Insert(cursor,period,date,student):
    if AVcheck(cursor,period,date) == True :
        return False
    else:
        Reserve(cursor,period,date,student)
        return True

def AVcheck(cursor,period,date):
    cursor.execute("SELECT COUNT(*) FROM Timetable WHERE Date = "+ date +" AND Period = "+ period +"")
    studentspresent = cursor.fetchone()[0]
    if studentspresent <= 20:
        return False
    else:
        return True

def Reserve(cursor,period,date,student):
    cursor.execute("INSERT into Timetable values('" + date + "','" + period + "','" + student + "')")
    cursor.execute("commit")

def Login(cursor,psw,email):
    global Invalid_cred
    try:
        cursor.execute("SELECT * FROM Users WHERE Email = " + email + " AND Password = " + psw + "")
        loggedperson = cursor.fetchone()
        if loggedperson:
            return True
    except ValueError as e:
        Invalid_cred.place(x=375, y=340, width=150, height=25)
        return False









