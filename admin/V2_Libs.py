from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import os
import tkinter.messagebox as message
import mysql.connector as mysql

#Connection variables

host="localhost"
user="sls-modifyer"
database="IA User-data"
Port=8889

#Functional subroutines

def isweekend(date_str):

    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_week = date_obj.weekday()
    if day_of_week < 5:
        return True
    else:
        return False

def IDtoName(ACCID):

    Data = connect(False,f"SELECT Name, Surname FROM Users WHERE AccID = {ACCID}")

    return Data[0],Data[1]

def getday(adder):
    today = datetime.today()
    future_date = today + timedelta(days=adder)
    return future_date.date()

def presentStatus(i,o,AccID):
    result = connect(False,f"SELECT Present FROM Timetable WHERE Period = '{o}' AND Date = '{getday(i)}' AND AccID ='{AccID}'")[0]
    if result == 1:
        return True,"Present"
    else:
        return False,"Not present"

def getTTstatus(i,o):

    result = connect(False,f"SELECT COUNT(*) AS count_entries FROM Timetable WHERE Period = '{o}' AND Date = '{getday(i)}'")[0]

    if result == 20:
        colour = "red"
    elif result >= 10 and result < 20:
        colour = "yellow"
    elif result >=0 and result < 10 :
        colour = "green"
    else:
        print("warning - exceeded max capacity")
        return

    result = f"{result}/20"

    return result,colour

def MedStatus(AccID):
    result=connect(False,f"SELECT Expiry FROM Certificates WHERE MedID = '{AccID}'")

    if result == None:
        return "Not submitted","red",True
    elif connect(False,f"SELECT Approved FROM Certificates WHERE MedID = '{AccID}'")[0] == 0:
        return "Not yet approved", "lightblue", False

    else:
        result=result[0]
        if getday(0) <= result <= getday(14):
            return f"Expires in {(result-getday(0)).days} days", "yellow",True

        elif result < getday(0):
            return "Expired", "red",False

        else:
            return "Submitted", "green",True

def ChangeMedStatus(AccID,LBL):
    if MedStatus(AccID)[2] == False:
        connect(False,f"UPDATE Certificates SET Approved = 1 WHERE MedID = '{AccID}' ")
        LBL.configure(text=MedStatus(AccID)[0],bg=MedStatus(AccID)[1])

    else:
        connect(False, f"UPDATE Certificates SET Approved = 0 WHERE MedID = '{AccID}' ")
        LBL.configure(text=MedStatus(AccID)[0],bg=MedStatus(AccID)[1])

def IndStatus(AccID):

    if connect(False,f"SELECT Induction FROM Users WHERE AccID = '{AccID}'")[0] == 0:
        return "Not completed","red", False
    else:
        return "Completed","green",True

def ChangeIndStatus(AccID,LBL):

    if IndStatus(AccID)[2] == False:
        connect(False,f"UPDATE Users SET Induction = 1 WHERE AccID = '{AccID}' ")
        LBL.configure(text=IndStatus(AccID)[0],bg=IndStatus(AccID)[1])

    else:
        connect(False, f"UPDATE Users SET Induction = 0 WHERE AccID = '{AccID}' ")
        LBL.configure(text=IndStatus(AccID)[0],bg=IndStatus(AccID)[1])

def TeachStatus(AccID):

    if connect(False,f"SELECT Teacher FROM Users WHERE AccID = '{AccID}'")[0] == 0:
        return "Student","lightblue",False
    else:
        return "Teacher","#8652B7",True

def ChangeTeachStatus(AccID,LBL):

    if TeachStatus(AccID)[2] == False:
        connect(False,f"UPDATE Users SET Teacher = 1 WHERE AccID = '{AccID}' ")
        LBL.configure(text=TeachStatus(AccID)[0],bg=TeachStatus(AccID)[1])

    else:
        connect(False, f"UPDATE Users SET Teacher = 0 WHERE AccID = '{AccID}' ")
        LBL.configure(text=TeachStatus(AccID)[0],bg=TeachStatus(AccID)[1])

def GetMedDate(AccID):
    if connect(False,f"SELECT * FROM Certificates WHERE MedID = {AccID}") != None:
        date = connect(False,f"SELECT Expiry FROM Certificates WHERE MedID = {AccID}")[0]
        formattedDate = date.strftime('%d/%m/%Y')
        return formattedDate

    else:
        return "--/--/----"

def AllStudentList():

    S_window = Tk()
    SpawnX = int((S_window.winfo_screenwidth() / 2) - (400 / 2))
    SpawnY = int((S_window.winfo_screenheight() / 2) - (400 / 2))
    S_window.title("Student Attendance")
    S_window.geometry(f"400x400+{SpawnX}+{SpawnY}")
    S_window.resizable(width=False, height=False)

    frame = Frame(S_window)
    frame.pack(fill=BOTH, expand=True)
    tree = ttk.Treeview(frame, columns=("Student",), show="headings")
    tree.heading("Student", text="Student")
    tree.column("Student", width=200, anchor=W)


    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(side=RIGHT, fill=Y)
    tree.pack(fill=BOTH, expand=True)

    students = AllStudents()
    counter = 0
    for student in students[1]:
        tree.insert("", "end", values=(student,))
        counter = counter + 1


    tree.bind("<Button-1>", lambda event: on_click(event, tree,students,None,None))


    S_window.mainloop()

def saveMed(pdf_data, filename):
    if pdf_data != None:

        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        pdf_file_path = os.path.join(downloads_folder, filename)

        with open(pdf_file_path, "wb") as pdf_file:
            pdf_file.write(pdf_data)
        message.showinfo("Download","Download completed succesfully")
    else:
        message.showinfo("Download", "No file found on database")

def getMedData(AccID):
    Data = connect(False,f"SELECT Image FROM Certificates WHERE MedID = '{AccID}'")[0]
    print(len(Data))
    return Data

def on_click(event,tree,students,o,i):
    region = tree.identify_region(event.x, event.y)
    item = tree.identify_row(event.y)
    column = tree.identify_column(event.x)



    if region == "cell":
        item_data = tree.item(item)
        student_name = item_data["values"][0]
        if o:
            present_status = item_data["values"][1]

        counter = 0
        for z in students[1]:
            if z == student_name:
                studentID = students[0][counter]
            counter = counter + 1

        if column == "#1":
            open_S_info(studentID)
        elif column == "#2":
            if connect(False,f"SELECT Present FROM Timetable WHERE Period = '{o}' AND Date = '{getday(i)}' AND AccID ='{studentID}'")[0] == 1:
                connect(False,f"UPDATE Timetable SET Present = 0 WHERE Period = '{o}' AND Date = '{getday(i)}' AND AccID ='{studentID}'")
                tree.item(item, values=(student_name, "Not present"))
            else:
                connect(False,f"UPDATE Timetable SET Present = 1 WHERE Period = '{o}' AND Date = '{getday(i)}' AND AccID ='{studentID}'")
                tree.item(item, values=(student_name, "Present"))

def S_in_period(i,o):

    AccId_List_Tuple = connect(True,f"SELECT AccID From Timetable WHERE Period = '{o}' AND Date = '{getday(i)}'")
    AccId_List = [item[0] for item in AccId_List_Tuple]
    AccName_List = []

    for ID in AccId_List:
        data = connect(False,f"SELECT Name, Surname FROM Users WHERE AccID = {ID}")
        Insertable = f"{data[0]} {data[1]}"
        AccName_List.append(Insertable)

    return AccId_List,AccName_List

def AllStudents():

    AccId_List_Tuple = connect(True,f"SELECT AccID From Users")
    AccId_List = [item[0] for item in AccId_List_Tuple]
    AccName_List = []

    for ID in AccId_List:
        data = connect(False,f"SELECT Name, Surname FROM Users WHERE AccID = {ID}")
        Insertable = f"{data[0]} {data[1]}"
        AccName_List.append(Insertable)

    return AccId_List,AccName_List

def connect(all,query):
    try:
        connection = mysql.connect(host=host, user=user, database=database, port=Port)
        cursor = connection.cursor()
        cursor.execute(query)

        if query.strip().upper().startswith(("INSERT", "DELETE", "UPDATE")):
            connection.commit()
        if query.strip().upper().startswith("SELECT"):
            if all == True:
                result = cursor.fetchall()
                return result
            else:
                result = cursor.fetchone()
                return result

    except Exception as e:
        message.showinfo("Connect failure", f"Error:{e}")
        return None

    finally:
        if cursor:
            cursor.fetchall()
            cursor.close()
        if connection:
            connection.close()

def deletefile(AccID,D_Label,S_Label):
    connect(False,f"DELETE FROM Certificates WHERE MedID = {AccID}")
    D_Label.configure(text=GetMedDate(AccID))
    S_Label.configure(text=MedStatus(AccID)[0], bg=MedStatus(AccID)[1])

def closewindow(window):
    window.destroy()

#Secondary page subroutines

def TTBTN_press(i, o):


    S_window = Tk()
    SpawnX = int((S_window.winfo_screenwidth() / 2) - (400 / 2))
    SpawnY = int((S_window.winfo_screenheight() / 2) - (400 / 2))
    S_window.title("Student Attendance")
    S_window.geometry(f"400x400+{SpawnX}+{SpawnY}")
    S_window.resizable(width=False, height=False)

    frame = Frame(S_window)
    frame.pack(fill=BOTH, expand=True)
    tree = ttk.Treeview(frame, columns=("Student", "Present"), show="headings")
    tree.heading("Student", text="Student")
    tree.heading("Present", text="Present")
    tree.column("Student", width=200, anchor=W)
    tree.column("Present", width=100, anchor=CENTER)

    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(side=RIGHT, fill=Y)
    tree.pack(fill=BOTH, expand=True)

    students = S_in_period(i, o)
    counter = 0
    for student in students[1]:
        tree.insert("", "end", values=(student, presentStatus(i,o,students[0][counter])[1]))
        counter = counter + 1


    tree.bind("<Button-1>", lambda event: on_click(event, tree,students,o,i))


    S_window.mainloop()

def open_S_info(AccID):
    SI_window = Tk()
    SpawnX = int((SI_window.winfo_screenwidth() / 2) - (600 / 2))
    SpawnY = int((SI_window.winfo_screenheight() / 2) - (430 / 2))
    SI_window.geometry(f"600x430+{SpawnX}+{SpawnY}")
    SI_window.title("Student Information")
    SI_window.resizable(width=False, height=False)

    TitleLabel = Label(SI_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                       text=f"{IDtoName(AccID)[0]} {IDtoName(AccID)[1]}'s Information")
    TitleLabel.place(x=0, y=0, width=600, height=70)

    QuitButton = Button(SI_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center", text="Exit",
                        command=lambda:closewindow(SI_window) )
    QuitButton.place(x=30, y=370, width=70, height=25)



    IND_Label = Label(SI_window, font=('Times', 20), fg="#333333", justify="center",
                      text=f"Induction day status:")
    IND_Label.place(x=30, y=75, width=250, height=50)

    IND_Status_Label = Label(SI_window, font=('Times', 20), fg="#333333", justify="center",
                             text=IndStatus(AccID)[0], bg=IndStatus(AccID)[1])
    IND_Status_Label.place(x=30, y=125, width=250, height=35)

    IND_Status_BTN = Button(SI_window, font=('Times', 20), fg="#333333", justify="center",text="Change",
                            command=lambda:ChangeIndStatus(AccID,IND_Status_Label))
    IND_Status_BTN.place(x=30, y=160, width=250, height=35)

    T_Label = Label(SI_window, font=('Times', 20), fg="#333333", justify="center",
                      text=f"Account status:")
    T_Label.place(x=30, y=225, width=250, height=50)

    T_Status_Label = Label(SI_window, font=('Times', 20), fg="#333333", justify="center",
                             text=TeachStatus(AccID)[0], bg=TeachStatus(AccID)[1])
    T_Status_Label.place(x=30, y=275, width=250, height=35)

    T_Status_BTN = Button(SI_window, font=('Times', 20), fg="#333333", justify="center",text="Change",
                          command=lambda:ChangeTeachStatus(AccID,T_Status_Label))
    T_Status_BTN.place(x=30, y=310, width=250, height=35)

    C_Label = Label(SI_window, font=('Times', 20), fg="#333333", justify="center",
                      text=f"Certificate status:")
    C_Label.place(x=310, y=75, width=250, height=50)

    C_Status_Label = Label(SI_window, font=('Times', 20), fg="#333333", justify="center",
                             text=MedStatus(AccID)[0], bg=MedStatus(AccID)[1])
    C_Status_Label.place(x=310, y=125, width=250, height=35)

    C_Status_BTN = Button(SI_window, font=('Times', 20), fg="#333333", justify="center",text="Approve",
                            command=lambda:ChangeMedStatus(AccID,C_Status_Label))
    C_Status_BTN.place(x=310, y=160, width=250, height=35)

    CD_Label = Label(SI_window, font=('Times', 20), fg="#333333", justify="center",
                      text=f"Expiry date:")
    CD_Label.place(x=310, y=225, width=250, height=50)

    CD_Status_Label = Label(SI_window, font=('Times', 20), fg="#333333", justify="center",
                             text=GetMedDate(AccID), bg="#efefef")
    CD_Status_Label.place(x=310, y=275, width=250, height=35)

    CD_Status_BTN = Button(SI_window, font=('Times', 20), fg="#333333", justify="center",text="Download",
                            command=lambda:saveMed(getMedData(AccID),f"{IDtoName(AccID)[0]} {IDtoName(AccID)[1]}'s certificate.pdf"))
    CD_Status_BTN.place(x=310, y=310, width=125, height=35)

    CD_Delete_BTN = Button(SI_window, font=('Times', 20), fg="#333333", justify="center", text="Delete proposal",
                           command=lambda: deletefile(AccID,CD_Status_Label,C_Status_Label))
    CD_Delete_BTN.place(x=435, y=310, width=125, height=35)


    SI_window.mainloop()





