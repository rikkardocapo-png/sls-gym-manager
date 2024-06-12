from tkinter import *
import tkinter.messagebox as message
import datetime as mysql



def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if id== "" or name== "" or phone== "":
        message.showinfo("Insert status","Some fields are empty")
    else:
        con = mysql.connect(host="localhost",user=loggeduser,password=loggedpass,database="python-tkinter",port=8889)
        cursor = con.cursor()
        cursor.execute("insert into student values('"+ id +"','"+ name +"','"+ phone +"')")
        cursor.execute("commit")

def delete():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if id== "" or name== "" or phone== "":
        message.showinfo("Delete status","Some fields are empty")
    else:
        con = mysql.connect(host="localhost",user=loggeduser,password=loggedpass,database="python-tkinter",port=8889)
        cursor = con.cursor()
        cursor.execute("DELETE FROM `student` WHERE `id`='" + id + "' AND `name`='" + name + "' AND `phone`='" + phone + "'")
        cursor.execute("commit")

def update():

    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if id == "" or name == "" or phone == "":
        message.showinfo("Update Status", "some fields are empty")
    else:
        connection = mysql.connect(host="localhost",user=loggeduser,password=loggedpass,database="python-tkinter",port=8889)
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE student set name='" + name + "', phone='" + phone + "' where id='" + id + "'")
        connection.commit()

        e_id.delete(0, "end")
        e_name.delete(0, "end")
        e_phone.delete(0, "end")
        message.showinfo("Update Status", "data successfully updated")
        connection.close()

def get():
    if e_id.get == "":
        message.showinfo("Get Status", "ID is necessary for operation")
    else:
        connection = mysql.connect(host="localhost",user=loggeduser,password=loggedpass,database="python-tkinter",port=8889)
        cursor = connection.cursor()
        cursor.execute("select * from student where id='" + e_id.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])

        connection.close()

def checkpresent(username):
    connection = mysql.connect(host="localhost",user="sls-modifyer",database="mysql",port=8889)

    try:
        cursor = connection.cursor()
        query = "SELECT user FROM mysql.user WHERE user = %s"
        cursor.execute(query, (username,))
        record = cursor.fetchone()

        return record

    except mysql.Error as e:
        print(f"Error: {e}")
        return None

    finally:
        if connection.is_connected():
            connection.close()

def signup():
    username = e_user.get()
    password = e_pass.get()

    if username == "" or password == "":
        message.showinfo("Insert status", "Some fields are empty")
    elif checkpresent(username) is not None:
        message.showinfo("Insert status", "Username taken")
    else:
        try:
            con = mysql.connect(host="localhost", user="sls-modifyer", database="python-tkinter", port=8889)
            cursor = con.cursor()
            cursor.execute(f"CREATE USER '{username}'@'%' IDENTIFIED WITH mysql_native_password BY '{password}';")
            cursor.execute(f"GRANT ALL PRIVILEGES ON *.* TO '{username}'@'%' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;")
            cursor.execute(f"GRANT ALL PRIVILEGES ON `python-tkinter`.* TO '{username}'@'%';")
            cursor.execute("COMMIT")

        except mysql.Error as e:
            print(f"Error: {e}")
            message.showinfo("Insert status", "Error creating user")

        finally:
            if con.is_connected():
                con.close()

def login():
    global loggeduser, loggedpass, SignUp_button, LGA_window, LG_window

    username = e_user.get()
    password = e_pass.get()

    if username == "" or password == "":
        message.showinfo("Get Status", "Some fields are empty")
    else:
        try:
            connection = mysql.connect(host="localhost", user=username, password=password, database="python-tkinter", port=8889)
            loggeduser = username
            loggedpass = password
            cursor = connection.cursor()
            if loggeduser=="admin":
                LG_window.destroy()
                openadminlogin()

            else:
                LG_window.destroy()
                openmanager()

        except mysql.Error as e:
            message.showinfo("Login status", "Wrong credentials")

def openadminlogin():
    global e_user, e_pass, LGA_window
    LGA_window=Tk()
    LGA_window.geometry("900x430")
    LGA_window.title("LOGIN-ADMIN")

    TitleLabel = Label(LGA_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                       text="Admin account manager")
    TitleLabel.place(x=225, y=60, width=450, height=70)

    Userlabel = Label(LGA_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",
                      text="Username:")
    Userlabel.place(x=360, y=170, width=180, height=35)

    e_user = Entry(LGA_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",
                   justify="center")
    e_user.place(x=360, y=205, width=180, height=35)

    Passlabel = Label(LGA_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",
                      text="Password:")
    Passlabel.place(x=360, y=270, width=180, height=35)

    e_pass = Entry(LGA_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",
                   justify="center", show="*")
    e_pass.place(x=360, y=305, width=180, height=35)

    QuitButton = Button(LGA_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center", text="Exit",
                        command=lambda: exit())
    QuitButton.place(x=30, y=370, width=70, height=25)

    Sign_Up_Button = Button(LGA_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center",
                            text="Create new account", command=lambda: signup())
    Sign_Up_Button.place(x=310, y=370, width=120, height=35)

    Sign_in_Button = Button(LGA_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center",
                            text="Sign-in as user", command=lambda: login())
    Sign_in_Button.place(x=450, y=370, width=120, height=35)

    LGA_window.mainloop()

def openlogin():
    global e_user, e_pass, LG_window
    LG_window = Tk()
    LG_window.geometry("900x430")
    LG_window.title("LOGIN")
    LG_window.resizable(width=False, height=False)

    TitleLabel = Label(LG_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                          text="Student contact manager")
    TitleLabel.place(x=225, y=60, width=450, height=70)

    Userlabel = Label(LG_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",
                          text="Username:")
    Userlabel.place(x=360, y=170, width=180, height=35)

    e_user = Entry(LG_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",
                   justify="center")
    e_user.place(x=360, y=205, width=180, height=35)

    Passlabel = Label(LG_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",
                          text="Password:")
    Passlabel.place(x=360, y=270, width=180, height=35)

    e_pass = Entry(LG_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",
                   justify="center", show="*")
    e_pass.place(x=360, y=305, width=180, height=35)

    QuitButton = Button(LG_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center", text="Exit",
                            command=lambda: exit())
    QuitButton.place(x=30, y=370, width=70, height=25)

    Sign_in_Button = Button(LG_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center",
                            text="Sign-in", command=lambda: login())
    Sign_in_Button.place(x=360, y=370, width=180, height=35)

    LG_window.mainloop()

def openmanager():
    global e_id, e_name, e_phone
    MM_window = Tk()
    MM_window.geometry("900x580")
    MM_window.title("WORKER MANAGER")
    MM_window.resizable(width=False, height=False)

    TitleLabel = Label(MM_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",text="Student contact manager")
    TitleLabel.place(x=225, y=60, width=450, height=70)


    e_id = Entry(MM_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",justify="center")
    e_id.place(x=360, y=205, width=180, height=35)
    e_name = Entry(MM_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333", justify="center")
    e_name.place(x=360, y=305, width=180, height=35)
    e_phone = Entry(MM_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333", justify="center")
    e_phone.place(x=360, y=405, width=180, height=35)

    Id = Label(MM_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",text="ID:")
    Id.place(x=360, y=270, width=180, height=35)
    Name = Label(MM_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center", text="Name:")
    Name.place(x=360, y=170, width=180, height=35)
    phone = Label(MM_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center", text="Phone:")
    phone.place(x=360, y=370, width=180, height=35)

    QuitButton = Button(MM_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center", text="Exit",
                        command=lambda: exit())
    QuitButton.place(x=30, y=525, width=70, height=25)

    Insert_Button = Button(MM_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center", text="Insert",command=lambda: insert())
    Insert_Button.place(x=250, y=470, width=80, height=35)

    Get_Button = Button(MM_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center",text="Get", command=lambda: get())
    Get_Button.place(x=350, y=470, width=80, height=35)

    Del_Button = Button(MM_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center", text="Delete",command=lambda: delete())
    Del_Button.place(x=450, y=470, width=80, height=35)

    Update_Button = Button(MM_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center", text="Update",command=lambda: update())
    Update_Button.place(x=550, y=470, width=80, height=35)

    MM_window.mainloop()


openlogin()