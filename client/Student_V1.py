import tkmacosx as btnx
from tkinter import *
from Studentapp.V1 import Student_Libs as Funcs

global e_user, e_pass
loggeduser=("")

# Startup functions

ACCID=1









#                  !
#                  !
# Window functions V - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def openlogin():
    global SU_window, LG_window, H_window, B_window
    PAGES=[SU_window, LG_window, H_window, B_window]
    try:
        SU_window.destroy()

    except:
        print("closure failed - 01")
        pass



    LG_window = Tk()
    SpawnX = int((LG_window.winfo_screenwidth() / 2)-(900/2))
    SpawnY = int((LG_window.winfo_screenheight() / 2)-(430/2))
    LG_window.geometry(f"900x430+{SpawnX}+{SpawnY}")
    LG_window.title("LOGIN")
    LG_window.resizable(width=False, height=False)

    TitleLabel = Label(LG_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                          text="SLS gym companion")
    TitleLabel.place(x=225, y=60, width=450, height=70)

    Userlabel = Label(LG_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",
                          text="E-mail:")
    Userlabel.place(x=360, y=170, width=180, height=35)

    e_user = Entry(LG_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",
                   justify="center", )
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
                            text="Sign-in", command=lambda: Funcs.login(str(e_user.get()),str(e_pass.get()),openHome))
    Sign_in_Button.place(x=360, y=370, width=180, height=35)

    Sign_up_Button = Button(LG_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center",
                            text="Sign-up", command=lambda: opensignup())
    Sign_up_Button.place(x=800, y=370, width=70, height=25)

    Invalid_cred = Label(LG_window,font=('Times', 10), fg="#FF0000", justify="center",text="Invalid credentials")
    """
    Invalid_cred.place(x=375, y=340, width=150, height=25)
    """
    LG_window.mainloop()

def opensignup():
    global LG_window, SU_window
    try:
        LG_window.destroy()
    except:
        pass
        print("closure failed - 02")
    SU_window = Tk()
    SpawnX = int((SU_window.winfo_screenwidth() / 2)-(900/2))
    SpawnY = int((SU_window.winfo_screenheight() / 2)-(430/2))
    SU_window.geometry(f"900x430+{SpawnX}+{SpawnY}")
    SU_window.title("SIGNUP")
    SU_window.resizable(width=False, height=False)

    TitleLabel = Label(SU_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                          text="Account Creation")
    TitleLabel.place(x=225, y=60, width=450, height=70)

    Userlabel = Label(SU_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",
                          text="E-mail:")
    Userlabel.place(x=210, y=170, width=180, height=35)

    e_user = Entry(SU_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",
                   justify="center")
    e_user.place(x=210, y=205, width=180, height=35)

    Passlabel = Label(SU_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",
                          text="Password:")
    Passlabel.place(x=210, y=270, width=180, height=35)

    e_pass = Entry(SU_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",
                   justify="center")
    e_pass.place(x=210, y=305, width=180, height=35)

    Namelabel = Label(SU_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",
                      text="Name:")
    Namelabel.place(x=510 , y=170, width=180, height=35)

    e_name = Entry(SU_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",
                   justify="center")
    e_name.place(x=510, y=205, width=180, height=35)

    Surlabel = Label(SU_window, bg="#efefef", font=('Times', 23), fg="#333333", justify="center",
                      text="Surname:")
    Surlabel.place(x=510, y=270, width=180, height=35)

    e_sur = Entry(SU_window, bg="#efefef", borderwidth="1px", font=('Times', 10), fg="#333333",
                   justify="center")
    e_sur.place(x=510, y=305, width=180, height=35)

    QuitButton = Button(SU_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center", text="Exit",
                            command=lambda: exit())
    QuitButton.place(x=30, y=370, width=70, height=25)

    Sign_in_Button = Button(SU_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center",
                            text="Sign-up", command=lambda: Funcs.signup(str(e_user.get()),str(e_pass.get()),str(e_name.get()),str(e_sur.get()),openlogin))
    Sign_in_Button.place(x=360, y=370, width=180, height=35)

    Sign_up_Button = Button(SU_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center",
                            text="Log-In", command=lambda: openlogin())
    Sign_up_Button.place(x=800, y=370, width=70, height=25)

    SU_window.mainloop()

def openHome(ACCID):
    global LG_Window, SU_window

    try:
        LG_window.destroy()
    except:
        pass
        print("closure failed - 03")

    H_window = Tk()
    SpawnX = int((H_window.winfo_screenwidth() / 2)-(900/2))
    SpawnY = int((H_window.winfo_screenheight() / 2)-(430/2))
    H_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
    H_window.title("HOME")
    H_window.resizable(width=False, height=False)

    TopLabel = Label(H_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                       text="SLS gym - Home")
    TopLabel.place(x=150 , y=0, width=750, height=75)

    Home_Button = btnx.Button(H_window,fg="#ebecf0", bg="#001b5e", font=('Times', 10), justify="center",
                            text="Home")
    Home_Button.place(x=0, y=0, width=150, height=75)

    Induction_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                         text="Induction")
    Induction_Button.place(x=0, y=75, width=150, height=75)

    Med_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                              text="Certificate")
    Med_Button.place(x=0, y=150, width=150, height=75)

    TMT_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                                  text="Bookings",command=lambda:openBook(ACCID))
    TMT_Button.place(x=0, y=225, width=150, height=75)

    Contact_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                        text="Contact")
    Contact_Button.place(x=0, y=300, width=150, height=75)

    Exit_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                            text="Exit",  command=lambda: exit())
    Exit_Button.place(x=0, y=375, width=150, height=75)

    """end of standard page -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -"""
    UserLabel = Label(H_window, font=('Times', 25), fg="#333333", justify="center",
                       text=f"Welcome back, {str(Funcs.IDtoName(ACCID))}")
    UserLabel.place(x=300 , y=150, width=450, height=75)

    Med_Label = Label(H_window, font=('Times', 20), fg="#333333", justify="center",
                      text=f"Certificate status:")
    Med_Label.place(x=155, y=275, width=350, height=75)

    Med_Status_Label = Label(H_window, font=('Times', 20), fg="#333333", justify="center",
                      text=f"IDK man")
    Med_Status_Label.place(x=155, y=350, width=350, height=75)

    IND_Label = Label(H_window, font=('Times', 20), fg="#333333", justify="center",
                      text=f"Induction day status:")
    IND_Label.place(x=525, y=275, width=350, height=75)

    IND_Status_Label = Label(H_window, font=('Times', 20), fg="#333333", justify="center",
                      text=f"IDK man")
    IND_Status_Label.place(x=525, y=350, width=350, height=75)

    H_window.mainloop()


def openBook(ACCID):
    global loggeduser, H_window

    try:
        H_window.destroy()
    except:
        pass
        print("closure failed - 03")

    B_window = Tk()
    SpawnX = int((B_window.winfo_screenwidth() / 2)-(900/2))
    SpawnY = int((B_window.winfo_screenheight() / 2)-(430/2))
    B_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
    B_window.title("HOME")
    B_window.resizable(width=False, height=False)

    TopLabel = Label(B_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                       text="SLS gym - Home")
    TopLabel.place(x=150 , y=0, width=750, height=75)

    Home_Button = btnx.Button(B_window,fg="#000000", bg="#4277fc", font=('Times', 10), justify="center",
                            text="Home",command=lambda:openHome(ACCID))
    Home_Button.place(x=0, y=0, width=150, height=75)

    Induction_Button = btnx.Button(B_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                         text="Induction")
    Induction_Button.place(x=0, y=75, width=150, height=75)

    Med_Button = btnx.Button(B_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                              text="Certificate")
    Med_Button.place(x=0, y=150, width=150, height=75)

    TMT_Button = btnx.Button(B_window, fg="#ebecf0", bg="#001b5e", justify="center",
                                  text="Bookings", font=('Times', 10))
    TMT_Button.place(x=0, y=225, width=150, height=75)

    Contact_Button = btnx.Button(B_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                        text="Contact")
    Contact_Button.place(x=0, y=300, width=150, height=75)

    Exit_Button = btnx.Button(B_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                            text="Exit",  command=lambda: exit())
    Exit_Button.place(x=0, y=375, width=150, height=75)

    Times=[" 14:00-15:00", "15:00- 16:00", "16:00-16:30", "16:45-17:15","17:15-18:00"]

    for i in range(7):
        TTLabel1 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",
                       text=Funcs.getday(i))
        TTLabel1.place(x=(i*75+300),y=(100),width=75,height=50)
        for o in range(5):
            if i == 0:
                TTLabel2 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",
                                 text=Times[o])
                TTLabel2.place(x=(225), y=(o*50+150), width=75, height=50)

            TTbutton = btnx.Button(B_window, text=Funcs.getTTstatus(i,o,ACCID)[0], bg=Funcs.getTTstatus(i,o,ACCID)[1])
            # command=lambda: Funcs.ttopen(i,o))
            TTbutton.place(x=(i*75+300),y=(o*50+150),width=75,height=50)




    B_window.mainloop()

openBook(1)