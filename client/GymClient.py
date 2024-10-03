import tkmacosx as btnx
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as message
from datetime import datetime, timedelta
import Student_Libs_V2 as Funcs


# Startup variables

SU_window=None
LG_window=None
H_window=None
B_window=None
C_window=None
I_window=None
M_window=None
filepath=None

# Window subroutines

def closewindows(windows):
    for window in windows:
        try:
            window.destroy()
        except:
            pass

def setup_themes():
    global style
    style = ttk.Style()

    # Style for selected window button
    style.configure("Side-select_button",
                    foreground="#ebecf0",
                    background="#001b5e",
                    font=('Times', 12),)

    # Style for non-selected window button
    style.configure("Side_button",
                    foreground="#000000",
                    background="#4277fc",
                    font=('Times', 12),)

    # Style for non-selected window button
    style.configure("Green_button",
                    foreground="#000000",
                    background="#4277fc",
                    font=('Times', 12), )

    style.map("Side_button",
             background=[("active", "#0056b3")])

def openBook(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window,M_window
    windows = [SU_window, LG_window, H_window, B_window, C_window, I_window,M_window]
    closewindows(windows)


    B_window = Tk()
    SpawnX = int((B_window.winfo_screenwidth() / 2)-(900/2))
    SpawnY = int((B_window.winfo_screenheight() / 2)-(430/2))
    B_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
    B_window.title("Bookings")
    B_window.resizable(width=False, height=False)

    TopLabel = Label(B_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                       text="SLS gym - Bookings")
    TopLabel.place(x=150 , y=0, width=750, height=75)

    Home_Button = btnx.Button(B_window,fg="#000000", bg="#4277fc", font=('Times', 10), justify="center",
                            text="Home",command=lambda:openHome(ACCID))
    Home_Button.place(x=0, y=0, width=150, height=75)

    Induction_Button = btnx.Button(B_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                         text="Induction",command=lambda: openInduction(ACCID))
    Induction_Button.place(x=0, y=75, width=150, height=75)

    Med_Button = btnx.Button(B_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                              text="Certificate",command=lambda: openMed(ACCID))
    Med_Button.place(x=0, y=150, width=150, height=75)

    TMT_Button = btnx.Button(B_window, fg="#ebecf0", bg="#001b5e", justify="center",
                                  text="Bookings", font=('Times', 10))
    TMT_Button.place(x=0, y=225, width=150, height=75)

    Contact_Button = btnx.Button(B_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                        text="Contact",command=lambda: openContact(ACCID))
    Contact_Button.place(x=0, y=300, width=150, height=75)

    Exit_Button = btnx.Button(B_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                            text="Exit",  command=lambda: exit())
    Exit_Button.place(x=0, y=375, width=150, height=75)

    Times=[" 14:00-15:00", "15:00- 16:00", "16:00-16:30", "16:45-17:15","17:15-18:00"]

    for i in range(7):
        TTLabel1 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",
                       text=Funcs.getday(i))
        TTLabel1.place(x=(i*75+300),y=(100),width=75,height=50)
        if Funcs.isweekend(str(Funcs.getday(i))) == True:
            for o in range(5):
                if i == 0:
                    TTLabel2 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",
                                     text=Times[o])
                    TTLabel2.place(x=(225), y=(o*50+150), width=75, height=50)

                TTbutton = btnx.Button(B_window, text=Funcs.getTTstatus(i,o,ACCID)[0], bg=Funcs.getTTstatus(i,o,ACCID)[1])
                TTbutton.place(x=(i*75+300),y=(o*50+150),width=75,height=50)
                TTbutton.configure(command=lambda i=i, o=o,btn=TTbutton: Funcs.TTBTN_press(i, o, ACCID,btn))
        else:
            for o in range(5):
                if i == 0:
                    TTLabel2 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",
                                     text=Times[o])
                    TTLabel2.place(x=(225), y=(o * 50 + 150), width=75, height=50)

                WElabel = Label(B_window,bg="grey")
                WElabel.place(x=(i * 75 + 300), y=(o * 50 + 150), width=75, height=50)


    B_window.mainloop()

def openlogin():
    global SU_window, LG_window, H_window, B_window, C_window, I_window
    windows = [SU_window, LG_window, H_window, B_window, C_window, I_window]



    LG_window = Tk()
    SpawnX = int((LG_window.winfo_screenwidth() / 2)-(900/2))
    SpawnY = int((LG_window.winfo_screenheight() / 2)-(430/2))
    LG_window.geometry(f"900x430+{SpawnX}+{SpawnY}")
    LG_window.title("Log-in")
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

    LG_window.after(40, closewindows,windows)

    LG_window.mainloop()

def opensignup():
    global SU_window, LG_window, H_window, B_window, C_window, I_window
    windows = [SU_window, LG_window, H_window, B_window, C_window, I_window]


    SU_window = Tk()
    SpawnX = int((SU_window.winfo_screenwidth() / 2)-(900/2))
    SpawnY = int((SU_window.winfo_screenheight() / 2)-(430/2))
    SU_window.geometry(f"900x430+{SpawnX}+{SpawnY}")
    SU_window.title("Sign-up")
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

    SU_window.after(40, closewindows, windows)

    SU_window.mainloop()

def openHome(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window
    windows = [SU_window, LG_window, H_window, B_window, C_window, I_window]

    H_window = Tk()
    SpawnX = int((H_window.winfo_screenwidth() / 2) - (900 / 2))
    SpawnY = int((H_window.winfo_screenheight() / 2) - (430 / 2))
    H_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
    H_window.title("Home")
    H_window.resizable(width=False, height=False)

    TopLabel = Label(H_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                     text="SLS gym - Home")
    TopLabel.place(x=150, y=0, width=750, height=75)

    Home_Button = btnx.Button(H_window, fg="#ebecf0", bg="#001b5e", font=('Times', 10), justify="center",
                              text="Home")
    Home_Button.place(x=0, y=0, width=150, height=75)

    Induction_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                                   text="Induction", command=lambda: openInduction(ACCID))
    Induction_Button.place(x=0, y=75, width=150, height=75)

    Med_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                             text="Certificate", command=lambda: openMed(ACCID))
    Med_Button.place(x=0, y=150, width=150, height=75)

    TMT_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                             text="Bookings", command=lambda: openBook(ACCID))
    TMT_Button.place(x=0, y=225, width=150, height=75)

    Contact_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                                 text="Contact", command=lambda: openContact(ACCID))
    Contact_Button.place(x=0, y=300, width=150, height=75)

    Exit_Button = btnx.Button(H_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                              text="Exit", command=lambda: exit())
    Exit_Button.place(x=0, y=375, width=150, height=75)

    UserLabel = Label(H_window, font=('Times', 30), fg="#333333", justify="center",
                      text=f"Welcome back, {str(Funcs.IDtoName(ACCID)[0])}")
    UserLabel.place(x=300, y=150, width=450, height=75)

    Med_Label = Label(H_window, font=('Times', 30), fg="#333333", justify="center",
                      text=f"Certificate status:")
    Med_Label.place(x=155, y=275, width=350, height=75)

    Med_Status_Label = Label(H_window, font=('Times', 20), fg="#333333", justify="center",
                             text=Funcs.MedStatus(ACCID)[0], bg=Funcs.MedStatus(ACCID)[1])
    Med_Status_Label.place(x=155, y=350, width=350, height=75)

    IND_Label = Label(H_window, font=('Times', 30), fg="#333333", justify="center",
                      text=f"Induction day status:")
    IND_Label.place(x=525, y=275, width=350, height=75)

    IND_Status_Label = Label(H_window, font=('Times', 20), fg="#333333", justify="center",
                             text=Funcs.IndStatus(ACCID)[0], bg=Funcs.IndStatus(ACCID)[1])
    IND_Status_Label.place(x=525, y=350, width=350, height=75)



    H_window.mainloop()


def openContact(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window,M_window,teacheremail,supportemail
    windows = [SU_window, LG_window, H_window, B_window, C_window, I_window,M_window]
    closewindows(windows)


    C_window = Tk()
    SpawnX = int((C_window.winfo_screenwidth() / 2) - (900 / 2))
    SpawnY = int((C_window.winfo_screenheight() / 2) - (430 / 2))
    C_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
    C_window.title("Contact")
    C_window.resizable(width=False, height=False)

    TopLabel = Label(C_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                     text="SLS gym - Contact ")
    TopLabel.place(x=150, y=0, width=750, height=75)

    Home_Button = btnx.Button(C_window, fg="#000000", bg="#4277fc", font=('Times', 10), justify="center",
                              text="Home",command=lambda: openHome(ACCID))
    Home_Button.place(x=0, y=0, width=150, height=75)

    Induction_Button = btnx.Button(C_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                                   text="Induction",command=lambda: openInduction(ACCID))
    Induction_Button.place(x=0, y=75, width=150, height=75)

    Med_Button = btnx.Button(C_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                             text="Certificate",command=lambda: openMed(ACCID))
    Med_Button.place(x=0, y=150, width=150, height=75)

    TMT_Button = btnx.Button(C_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                             text="Bookings", command=lambda: openBook(ACCID))
    TMT_Button.place(x=0, y=225, width=150, height=75)

    Contact_Button = btnx.Button(C_window, bg="#001b5e",fg="#FFFFFF", font=('Times', 10), justify="center",
                                 text="Contact")
    Contact_Button.place(x=0, y=300, width=150, height=75)

    Exit_Button = btnx.Button(C_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                              text="Exit", command=lambda: exit())
    Exit_Button.place(x=0, y=375, width=150, height=75)

    TeacherLabel = Label(C_window, bg="#FFFFFF", font=('Times', 30), fg="#333333", justify="center",
                     text="Gym teacher reference: ")
    TeacherLabel.place(x=200, y=175, width=300, height=50)

    SupportLabel = Label(C_window, bg="#FFFFFF", font=('Times', 30), fg="#333333", justify="center",
                         text="Tech support reference: ")
    SupportLabel.place(x=200, y=275, width=300, height=50)

    Teacher_Button = btnx.Button(C_window, bg="#FFFFFF", font=('Times', 30), fg="#000000", justify="center",
                              text="Send message", command=lambda: Funcs.sendemail(teacheremail,ACCID,None))
    Teacher_Button.place(x=500, y=175, width=300, height=50)

    Support_Button = btnx.Button(C_window, bg="#FFFFFF", font=('Times', 30), fg="#000000", justify="center",
                              text="Send message", command=lambda: Funcs.sendemail(supportemail,ACCID,None))
    Support_Button.place(x=500, y=275, width=300, height=50)

def openInduction(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window,M_window
    windows = [SU_window, LG_window, H_window, B_window, C_window, I_window,M_window]
    closewindows(windows)


    I_window = Tk()
    SpawnX = int((I_window.winfo_screenwidth() / 2) - (900 / 2))
    SpawnY = int((I_window.winfo_screenheight() / 2) - (430 / 2))
    I_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
    I_window.title("Induction")
    I_window.resizable(width=False, height=False)

    TopLabel = Label(I_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                     text="SLS gym - Induction ")
    TopLabel.place(x=150, y=0, width=750, height=75)

    Home_Button = btnx.Button(I_window, fg="#000000", bg="#4277fc", font=('Times', 10), justify="center",
                              text="Home",command=lambda: openHome(ACCID))
    Home_Button.place(x=0, y=0, width=150, height=75)

    Induction_Button = btnx.Button(I_window, bg="#001b5e", font=('Times', 10), fg="#FFFFFF", justify="center",
                                   text="Induction")
    Induction_Button.place(x=0, y=75, width=150, height=75)

    Med_Button = btnx.Button(I_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                             text="Certificate",command=lambda: openMed(ACCID))
    Med_Button.place(x=0, y=150, width=150, height=75)

    TMT_Button = btnx.Button(I_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                             text="Bookings", command=lambda: openBook(ACCID))
    TMT_Button.place(x=0, y=225, width=150, height=75)

    Contact_Button = btnx.Button(I_window, bg="#4277fc",fg="#000000", font=('Times', 10), justify="center",
                                 text="Contact",command=lambda: openContact(ACCID))
    Contact_Button.place(x=0, y=300, width=150, height=75)

    Exit_Button = btnx.Button(I_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                              text="Exit", command=lambda: exit())
    Exit_Button.place(x=0, y=375, width=150, height=75)

    ScriptLabel = Label(I_window, bg="#FFFFFF", font=('Times', 30), fg="#333333", justify="center",
                     text="Induction days are appointed by the gym manager, contact below:",wraplength=600)
    ScriptLabel.place(x=215, y=150, width=600, height=100)

    Teacher_Button = btnx.Button(I_window, bg="#FFFFFF", font=('Times', 30), fg="#000000", justify="center",
                              text="Send message", command=lambda: Funcs.sendemail(teacheremail,ACCID,True))
    Teacher_Button.place(x=360, y=250, width=300, height=50)

def openMed(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window,M_window
    windows = [SU_window, LG_window, H_window, B_window, C_window, I_window,M_window]
    closewindows(windows)


    M_window = Tk()
    SpawnX = int((M_window.winfo_screenwidth() / 2) - (900 / 2))
    SpawnY = int((M_window.winfo_screenheight() / 2) - (430 / 2))
    M_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
    M_window.title("Certificate")
    M_window.resizable(width=False, height=False)

    TopLabel = Label(M_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                     text="SLS gym - Certificate ")
    TopLabel.place(x=150, y=0, width=750, height=75)

    Home_Button = btnx.Button(M_window, fg="#000000", bg="#4277fc", font=('Times', 10), justify="center",
                              text="Home",command=lambda: openHome(ACCID))
    Home_Button.place(x=0, y=0, width=150, height=75)

    Induction_Button = btnx.Button(M_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                                   text="Induction",command=lambda: openInduction(ACCID))
    Induction_Button.place(x=0, y=75, width=150, height=75)

    Med_Button = btnx.Button(M_window, bg="#001b5e", font=('Times', 10), fg="#FFFFFF", justify="center",
                             text="Certificate")
    Med_Button.place(x=0, y=150, width=150, height=75)

    TMT_Button = btnx.Button(M_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                             text="Bookings", command=lambda: openBook(ACCID))
    TMT_Button.place(x=0, y=225, width=150, height=75)

    Contact_Button = btnx.Button(M_window, bg="#4277fc",fg="#000000", font=('Times', 10), justify="center",
                                 text="Contact",command=lambda: openContact(ACCID))
    Contact_Button.place(x=0, y=300, width=150, height=75)

    Exit_Button = btnx.Button(M_window, bg="#4277fc", font=('Times', 10), fg="#000000", justify="center",
                              text="Exit", command=lambda: exit())
    Exit_Button.place(x=0, y=375, width=150, height=75)

    ScriptLabel = Label(M_window, bg="#FFFFFF", font=('Times', 30), fg="#333333", justify="center",
                     text="Select new certificate below:",wraplength=600)
    ScriptLabel.place(x=215, y=100, width=600, height=50)

    Select_Button = btnx.Button(M_window, bg="#FFFFFF", font=('Times', 30), fg="#000000", justify="center",
                              text="Select file", command=lambda: Funcs.select_file(Select_Button))
    Select_Button.place(x=360, y=150, width=300, height=50)

    MedTB = Entry(M_window, bg="#FFFFFF", font=('Times', 30), fg="#333333", justify="center",)

    MedTB.place(x=365, y=275, width=300, height=50)

    DateLabel = Label(M_window, bg="#FFFFFF", font=('Times', 30), fg="#333333", justify="center",
                      text="Insert expiry date:", wraplength=600)
    DateLabel.place(x=215, y=225, width=600, height=50)

    Upload_Button = btnx.Button(M_window, bg="#FFFFFF", font=('Times', 30), fg="#000000", justify="center",
                              text="Upload Certificate", command=lambda: Funcs.upload_file(MedTB,ACCID))
    Upload_Button.place(x=360, y=350, width=300, height=50)



if __name__ == "__main__":
    openlogin()
