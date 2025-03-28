


# Importing libraries
# These libraries are required dependencies for some of the functions below
from tkinter import *
import Student_Libs as Funcs
import tkinter as tk
from tkinter import ttk
import atexit


# Startup variables
# These variables are initialized beforehand to make the system orderly and also to make the program easier to translate to something like C++
SU_window = None
LG_window = None
H_window = None
B_window = None
C_window = None
I_window = None
M_window = None
filepath = None
style = None
TTbuttons = {}
H_IND_Status_Label = None
H_Med_Status_Label = None
teacheremail="gym-staff@example.com"
supportemail="rcapobianco@stlouisschoolapps.com"



# Window subroutines

def setup_styles():
    global style
    # This crucial function initializes the button styles for the entire application. This is required especially for the coloured booking timetable
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Menu.TButton', background='#FFFFFF', foreground='#333333', padding=5)
    style.map('Menu.TButton',
              background=[('active', '#8a8a8a'), ('pressed', 'deepskyblue')])

    style.configure('Menu2.TButton', background='#FFFFFF', foreground='#333333', padding=5, font=("Poppins",30))
    style.map('Menu2.TButton',
              background=[('active', '#8a8a8a'), ('pressed', 'deepskyblue')])

    style.configure('Menu3.TButton', background='#eb5841', foreground='#333333', padding=5, font=('Poppins', 15))
    style.map('Menu3.TButton',
              background=[('active', '#8a8a8a')])

    style.configure('ToolBA.TButton', background='#001b5e', foreground='#ebecf0', padding=5)
    style.map('ToolBA.TButton',
              background=[('active', '#2b4e94'), ('pressed', 'deepskyblue')])

    style.configure('ToolB.TButton', background='#4277fc', foreground='#000000', padding=5)
    style.map('ToolB.TButton',
              background=[('active', '#88affc'), ('pressed', 'deepskyblue')])

    style.configure('Red.TButton', background='red', foreground='#000000', padding=5)
    style.map('Red.TButton',
              background=[('active', '#f57373'), ('pressed', 'deepskyblue')])

    style.configure('Green.TButton', background='green', foreground='#000000', padding=5)
    style.map('Green.TButton',
              background=[('active', '#3cab59'), ('pressed', 'deepskyblue')])

    style.configure('Yellow.TButton', background='yellow', foreground='#000000', padding=5)
    style.map('Yellow.TButton',
              background=[('active', '#ebe698'), ('pressed', 'deepskyblue')])

    style.configure('Purple.TButton', background='purple', foreground='#000000', padding=5)
    style.map('Purple.TButton',
              background=[('active', '#9c59b5'), ('pressed', 'deepskyblue')])

    style.configure('Grey.TButton', background='grey', foreground='#000000', padding=5)
    style.map('Purple.TButton',
              background=[('active', '#9c59b5'), ('pressed', 'black')])

def closewindows(windows):
    # This function withdraws any open window
    for i in range(len(windows)):
        try:
            windows[i].withdraw()

        except:
            pass

def refresh_buttons(ACCID):
    global TTbuttons
    #This function refreshes the timetable by individually configuring every button tstored in the TTbuttons 2d array
    for i in range(7):
        for o in range(5):
            btn = TTbuttons.get((i, o))

            if btn:
                if not Funcs.isweekend(str(Funcs.getday(i))):
                    btn.configure(text="", style="Grey.TButton", state="disabled")
                else:
                    text, style = Funcs.getTTstatus(i, o, ACCID)
                    btn.configure(text=text, style=style, state="normal")

def QuitApp():
    global LG_window
    # Pretty self explanatory, kills the toplevel window and therefore the whole app collaplses and shuts down
    LG_window.destroy()

def openlogin():
    global SU_window, LG_window, H_window, B_window, C_window, I_window, style
    windows = [SU_window, H_window, B_window, C_window, I_window, ]
    # This function opens the login window GUI or, if already stored, shows it. It then hides the previous window to give an idea of continuity
    if LG_window is None:
        LG_window = tk.Tk()
        setup_styles()
        SpawnX = int((LG_window.winfo_screenwidth() / 2) - (900 / 2))
        SpawnY = int((LG_window.winfo_screenheight() / 2) - (430 / 2))
        LG_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
        LG_window.title("Log-in")

        LG_window.resizable(width=False, height=False)

        LG_TitleLabel = tk.Label(LG_window, background="#eb5841", font=('Poppins', 38), foreground="#333333", justify="center",
                                 text="SLS gym companion")
        LG_TitleLabel.place(x=225, y=60, width=450, height=70)

        LG_Userlabel = tk.Label(LG_window, background="#FFFFFF", font=('Poppins', 23), foreground="#333333", justify="center",
                                 text="E-mail:")
        LG_Userlabel.place(x=360, y=170, width=180, height=35)

        LG_e_user = tk.Entry(LG_window, background="#FFFFFF", borderwidth="1px", font=('Poppins', 10), foreground="#333333",
                             justify="center")
        LG_e_user.place(x=360, y=205, width=180, height=35)

        LG_Passlabel = tk.Label(LG_window, background="#FFFFFF", font=('Poppins', 23), foreground="#333333", justify="center",
                                 text="Password:")
        LG_Passlabel.place(x=360, y=270, width=180, height=35)

        LG_e_pass = tk.Entry(LG_window, background="#FFFFFF", borderwidth="1px", font=('Poppins', 10), foreground="#333333",
                             justify="center", show="*")
        LG_e_pass.place(x=360, y=305, width=180, height=35)

        LG_QuitButton = ttk.Button(LG_window, text="Exit", style='Menu.TButton', command=lambda: QuitApp())

        LG_QuitButton.place(x=30, y=370, width=70, height=25)

        LG_Sign_in_Button = ttk.Button(LG_window, text="Sign-in", style='Menu.TButton',
                                       command=lambda: Funcs.login(str(LG_e_user.get()), str(LG_e_pass.get()), openHome))
        LG_Sign_in_Button.place(x=360, y=370, width=180, height=35)

        LG_Sign_up_Button = ttk.Button(LG_window, text="Sign-up", style='Menu.TButton',
                                       command=lambda: opensignup())
        LG_Sign_up_Button.place(x=800, y=370, width=70, height=25)

        LG_window.after(60, closewindows, windows)
        LG_window.mainloop()

    else:
        LG_window.deiconify()
        closewindows(windows)

def opensignup():
    global SU_window, LG_window, H_window, B_window, C_window, I_window, style
    windows = [LG_window, H_window, B_window, C_window, I_window, M_window, ]
    # This function opens the signup window GUI or, if already stored, shows it. It then hides the previous window to give an idea of continuity
    if SU_window is None:
        SU_window = tk.Toplevel(LG_window)
        setup_styles()
        SpawnX = int((SU_window.winfo_screenwidth() / 2) - (900 / 2))
        SpawnY = int((SU_window.winfo_screenheight() / 2) - (430 / 2))
        SU_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
        SU_window.title("Sign-up")
        SU_window.resizable(width=False, height=False)

        SU_TitleLabel = tk.Label(SU_window, background="#eb5841", font=('Poppins', 38), foreground="#333333", justify="center",
                                 text="Account Creation")
        SU_TitleLabel.place(x=225, y=60, width=450, height=70)

        SU_Userlabel = tk.Label(SU_window, background="#FFFFFF", font=('Poppins', 23), foreground="#333333", justify="center",
                                 text="E-mail:")
        SU_Userlabel.place(x=210, y=170, width=180, height=35)

        SU_e_user = tk.Entry(SU_window, background="#FFFFFF", borderwidth="1px", font=('Poppins', 10), foreground="#333333",
                             justify="center")
        SU_e_user.place(x=210, y=205, width=180, height=35)

        SU_Passlabel = tk.Label(SU_window, background="#FFFFFF", font=('Poppins', 23), foreground="#333333", justify="center",
                                 text="Password:")
        SU_Passlabel.place(x=210, y=270, width=180, height=35)

        SU_e_pass = tk.Entry(SU_window, background="#FFFFFF", borderwidth="1px", font=('Poppins', 10), foreground="#333333",
                             justify="center")
        SU_e_pass.place(x=210, y=305, width=180, height=35)

        SU_Namelabel = tk.Label(SU_window, background="#FFFFFF", font=('Poppins', 23), foreground="#333333", justify="center",
                                text="Name:")
        SU_Namelabel.place(x=510, y=170, width=180, height=35)

        SU_e_name = tk.Entry(SU_window, background="#FFFFFF", borderwidth="1px", font=('Poppins', 10), foreground="#333333",
                             justify="center")
        SU_e_name.place(x=510, y=205, width=180, height=35)

        SU_Surlabel = tk.Label(SU_window, background="#FFFFFF", font=('Poppins', 23), foreground="#333333", justify="center",
                               text="Surname:")
        SU_Surlabel.place(x=510, y=270, width=180, height=35)

        SU_e_sur = tk.Entry(SU_window, background="#FFFFFF", borderwidth="1px", font=('Poppins', 10), foreground="#333333",
                            justify="center")
        SU_e_sur.place(x=510, y=305, width=180, height=35)

        SU_QuitButton = ttk.Button(SU_window, text="Exit", style='Menu.TButton', command=lambda: QuitApp())

        SU_QuitButton.place(x=30, y=370, width=70, height=25)

        SU_Sign_in_Button = ttk.Button(SU_window, text="Sign-up", style='Menu.TButton',
                                       command=lambda: Funcs.signup(str(SU_e_user.get()), str(SU_e_pass.get()), str(SU_e_name.get()), str(SU_e_sur.get()), openlogin))
        SU_Sign_in_Button.place(x=360, y=370, width=180, height=35)

        SU_Sign_up_Button = ttk.Button(SU_window, text="Log-In", style='Menu.TButton',
                                       command=lambda: openlogin())
        SU_Sign_up_Button.place(x=800, y=370, width=70, height=25)

        SU_window.after(60, closewindows, windows)
        SU_window.mainloop()
    else:
        SU_window.deiconify()
        closewindows(windows)

def openHome(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window, M_window, H_IND_Status_Label,H_Med_Status_Label
    windows = [SU_window, LG_window, B_window, C_window, I_window, M_window, ]
    # This function opens the Home window GUI or, if already stored, shows it. It then hides the previous window to give an idea of continuity
    if H_window == None:
        H_window = tk.Toplevel(LG_window)
        SpawnX = int((H_window.winfo_screenwidth() / 2)-(900/2))
        SpawnY = int((H_window.winfo_screenheight() / 2)-(430/2))
        H_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
        H_window.title("Home")
        H_window.resizable(width=False, height=False)

        H_TopLabel = Label(H_window, background="#eb5841", font=('Poppins', 38), foreground="#333333", justify="center",
                           text="SLS gym - Home")
        H_TopLabel.place(x=150 , y=0, width=750, height=75)

        H_Home_Button = ttk.Button(H_window, style="ToolBA.TButton", text="Home")
        H_Home_Button.place(x=0, y=0, width=150, height=75)

        H_Induction_Button = ttk.Button(H_window, style="ToolB.TButton", text="Induction", command=lambda: openInduction(ACCID))
        H_Induction_Button.place(x=0, y=75, width=150, height=75)

        H_Med_Button = ttk.Button(H_window, style="ToolB.TButton", text="Certificate", command=lambda: openMed(ACCID))
        H_Med_Button.place(x=0, y=150, width=150, height=75)

        H_TMT_Button = ttk.Button(H_window, style="ToolB.TButton", text="Bookings", command=lambda: openBook(ACCID))
        H_TMT_Button.place(x=0, y=225, width=150, height=75)

        H_Contact_Button = ttk.Button(H_window, style="ToolB.TButton", text="Contact", command=lambda: openContact(ACCID))
        H_Contact_Button.place(x=0, y=300, width=150, height=75)

        H_Exit_Button = ttk.Button(H_window, style="ToolB.TButton", text="Exit", command=lambda: QuitApp())
        H_Exit_Button.place(x=0, y=375, width=150, height=75)

        """end of standard page -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -"""

        H_UserLabel = Label(H_window, font=('Poppins', 30), foreground="#333333", justify="center",
                           text=f"Welcome back, {str(Funcs.IDtoName(ACCID)[0])}")
        H_UserLabel.place(x=300 , y=150, width=450, height=75)

        H_Med_Label = Label(H_window, font=('Poppins', 30), foreground="#333333", justify="center",
                          text=f"Certificate status:")
        H_Med_Label.place(x=155, y=275, width=350, height=75)

        H_Med_Status_Label = Label(H_window, font=('Poppins', 20), foreground="#333333", justify="center",
                          text=Funcs.MedStatus(ACCID)[0], background=Funcs.MedStatus(ACCID)[1])
        H_Med_Status_Label.place(x=155, y=350, width=350, height=75)

        H_IND_Label = Label(H_window, font=('Poppins', 30), foreground="#333333", justify="center",
                          text=f"Induction day status:")
        H_IND_Label.place(x=525, y=275, width=350, height=75)

        H_IND_Status_Label = Label(H_window, font=('Poppins', 20), foreground="#333333", justify="center",
                          text=Funcs.IndStatus(ACCID)[0], background=Funcs.IndStatus(ACCID)[1])
        H_IND_Status_Label.place(x=525, y=350, width=350, height=75)

        H_window.after(60, closewindows, windows)

        H_window.mainloop()

    else:
        H_window.deiconify()
        H_Med_Status_Label.configure(text=Funcs.MedStatus(ACCID)[0], background=Funcs.MedStatus(ACCID)[1])
        H_IND_Status_Label.configure(text=Funcs.IndStatus(ACCID)[0], background=Funcs.IndStatus(ACCID)[1])

        closewindows(windows)

def openBook(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window, M_window, TTbuttons
    windows = [SU_window, LG_window, H_window, C_window, I_window, M_window, ]
    # This function opens the Bookings window GUI or, if already stored, shows it. It then hides the previous window to give an idea of continuity
    # This function is the core element of the app and uses a if statement with two double nested loops to create the timetable the first time. The buttons are then stored with my [i:o] coordinate system in a 2d array called TTbuttons
    if B_window == None:
        B_window = tk.Toplevel(LG_window)
        SpawnX = int((B_window.winfo_screenwidth() / 2)-(900/2))
        SpawnY = int((B_window.winfo_screenheight() / 2)-(430/2))
        B_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
        B_window.title("Bookings")
        B_window.resizable(width=False, height=False)

        B_TopLabel = Label(B_window, background="#eb5841", font=('Poppins', 38), foreground="#333333", justify="center",text="SLS gym - Bookings")
        B_TopLabel.place(x=150, y=0, width=750, height=75)

        B_Home_Button = ttk.Button(B_window, style="ToolB.TButton", text="Home", command=lambda: openHome(ACCID))
        B_Home_Button.place(x=0, y=0, width=150, height=75)

        B_Induction_Button = ttk.Button(B_window, style="ToolB.TButton", text="Induction", command=lambda: openInduction(ACCID))
        B_Induction_Button.place(x=0, y=75, width=150, height=75)

        B_Med_Button = ttk.Button(B_window, style="ToolB.TButton", text="Certificate", command=lambda: openMed(ACCID))
        B_Med_Button.place(x=0, y=150, width=150, height=75)

        B_TMT_Button = ttk.Button(B_window, style="ToolBA.TButton", text="Bookings")
        B_TMT_Button.place(x=0, y=225, width=150, height=75)

        B_Contact_Button = ttk.Button(B_window, style="ToolB.TButton", text="Contact", command=lambda: openContact(ACCID))
        B_Contact_Button.place(x=0, y=300, width=150, height=75)

        B_Exit_Button = ttk.Button(B_window, style="ToolB.TButton", text="Exit", command=lambda: QuitApp())
        B_Exit_Button.place(x=0, y=375, width=150, height=75)

        Rbutton = ttk.Button(B_window, text="Refresh", style="Menu3.TButton",command=lambda: refresh_buttons(ACCID))
        Rbutton.place(x=(225), y=(100), width=75, height=50)

        Time=[" 14:00-15:00", "15:00- 16:00", "16:00-16:30", "16:45-17:15","17:15-18:00"]

        for i in range(7):
            B_TTLabel1 = Label(B_window, background="#eb5841", font=('Poppins', 10), foreground="#333333", justify="center",
                           text=Funcs.getday(i))
            B_TTLabel1.place(x=(i*75+300),y=(100),width=75,height=50)
            if Funcs.isweekend(str(Funcs.getday(i))) == True:
                for o in range(5):
                    if i == 0:
                        B_TTLabel2 = Label(B_window, background="#eb5841", font=('Poppins', 10), foreground="#333333", justify="center",
                                         text=Time[o])
                        B_TTLabel2.place(x=(225), y=(o*50+150), width=75, height=50)

                    B_TTbutton = ttk.Button(B_window, text=Funcs.getTTstatus(i,o,ACCID)[0], style=Funcs.getTTstatus(i,o,ACCID)[1])
                    B_TTbutton.configure(command=lambda i=i, o=o, btn=B_TTbutton: Funcs.TTBTN_press(i, o, ACCID,btn))
                    B_TTbutton.place(x=(i * 75 + 300), y=(o * 50 + 150), width=75, height=50)
                    TTbuttons[(i, o)] = B_TTbutton
            else:
                for o in range(5):
                    if i == 0:
                        B_TTLabel2 = Label(B_window, background="#eb5841", font=('Poppins', 10), foreground="#333333", justify="center",
                                         text=Time[o])
                        B_TTLabel2.place(x=(225), y=(o * 50 + 150), width=75, height=50)

                    B_TTbutton = ttk.Button(B_window, text="",style="Grey.TButton",state="disabled")
                    B_TTbutton.place(x=(i * 75 + 300), y=(o * 50 + 150), width=75, height=50)
                    TTbuttons[(i, o)] = B_TTbutton

        B_window.after(60, closewindows, windows)

        B_window.mainloop()

    else:

        B_window.deiconify()

        closewindows(windows)

def openContact(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window, M_window, teacheremail, supportemail
    windows = [SU_window, LG_window, H_window, B_window, I_window, M_window, ]
    # This function opens the contact window GUI or, if already stored, shows it. It then hides the previous window to give an idea of continuity
    if C_window == None:
        C_window = tk.Toplevel(LG_window)
        SpawnX = int((C_window.winfo_screenwidth() / 2) - (900 / 2))
        SpawnY = int((C_window.winfo_screenheight() / 2) - (430 / 2))
        C_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
        C_window.title("Contact")
        C_window.resizable(width=False, height=False)

        C_TopLabel = Label(C_window, background="#eb5841", font=('Poppins', 38), foreground="#333333", justify="center",
                           text="SLS gym - Contact ")
        C_TopLabel.place(x=150, y=0, width=750, height=75)

        C_Home_Button = ttk.Button(C_window, style="ToolB.TButton", text="Home", command=lambda: openHome(ACCID))
        C_Home_Button.place(x=0, y=0, width=150, height=75)

        C_Induction_Button = ttk.Button(C_window, style="ToolB.TButton",  text="Induction", command=lambda: openInduction(ACCID))
        C_Induction_Button.place(x=0, y=75, width=150, height=75)

        C_Med_Button = ttk.Button(C_window, style="ToolB.TButton",  text="Certificate", command=lambda: openMed(ACCID))
        C_Med_Button.place(x=0, y=150, width=150, height=75)

        C_TMT_Button = ttk.Button(C_window, style="ToolB.TButton",  text="Bookings", command=lambda: openBook(ACCID))
        C_TMT_Button.place(x=0, y=225, width=150, height=75)

        C_Contact_Button = ttk.Button(C_window, style="ToolBA.TButton",  text="Contact")
        C_Contact_Button.place(x=0, y=300, width=150, height=75)

        C_Exit_Button = ttk.Button(C_window, style="ToolB.TButton",  text="Exit", command=lambda: QuitApp())
        C_Exit_Button.place(x=0, y=375, width=150, height=75)

        C_TeacherLabel = Label(C_window, background="#FFFFFF", font=('Poppins', 30), foreground="#333333", justify="center",text="Gym teacher reference: ")
        C_TeacherLabel.place(x=175, y=175, width=325, height=50)

        C_SupportLabel = Label(C_window, background="#FFFFFF", font=('Poppins', 30), foreground="#333333", justify="center",text="Tech support reference: ")
        C_SupportLabel.place(x=175, y=275, width=325, height=50)

        C_Teacher_Button = ttk.Button(C_window, style="Menu2.TButton",  text="Send message", command=lambda: Funcs.sendemail(teacheremail, ACCID, None))
        C_Teacher_Button.place(x=500, y=175, width=300, height=50)

        C_Support_Button = ttk.Button(C_window, style="Menu2.TButton",  text="Send message", command=lambda: Funcs.sendemail(supportemail, ACCID, None))
        C_Support_Button.place(x=500, y=275, width=300, height=50)


        C_window.after(60, closewindows, windows)

        C_window.mainloop()

    else:
        C_window.deiconify()

        closewindows(windows)

def openInduction(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window, M_window
    windows = [SU_window, LG_window, H_window, B_window, C_window, M_window, ]
    # This function opens the Induction window GUI or, if already stored, shows it. It then hides the previous window to give an idea of continuity
    if I_window == None:
        I_window = tk.Toplevel(LG_window)
        SpawnX = int((I_window.winfo_screenwidth() / 2) - (900 / 2))
        SpawnY = int((I_window.winfo_screenheight() / 2) - (430 / 2))
        I_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
        I_window.title("Induction")
        I_window.resizable(width=False, height=False)

        I_TopLabel = Label(I_window, background="#eb5841", foreground="#333333", text="SLS gym - Induction ", font=('Poppins', 38))
        I_TopLabel.place(x=150, y=0, width=750, height=75)

        I_Home_Button = ttk.Button(I_window, style="ToolB.TButton", text="Home", command=lambda: openHome(ACCID))
        I_Home_Button.place(x=0, y=0, width=150, height=75)

        I_Induction_Button = ttk.Button(I_window, style="ToolBA.TButton", text="Induction")
        I_Induction_Button.place(x=0, y=75, width=150, height=75)

        I_Med_Button = ttk.Button(I_window, style="ToolB.TButton", text="Certificate", command=lambda: openMed(ACCID))
        I_Med_Button.place(x=0, y=150, width=150, height=75)

        I_TMT_Button = ttk.Button(I_window, style="ToolB.TButton", text="Bookings", command=lambda: openBook(ACCID))
        I_TMT_Button.place(x=0, y=225, width=150, height=75)

        I_Contact_Button = ttk.Button(I_window, style="ToolB.TButton", text="Contact", command=lambda: openContact(ACCID))
        I_Contact_Button.place(x=0, y=300, width=150, height=75)

        I_Exit_Button = ttk.Button(I_window, style="ToolB.TButton", text="Exit", command=lambda: QuitApp())
        I_Exit_Button.place(x=0, y=375, width=150, height=75)

        I_ScriptLabel = Label(I_window, background="#FFFFFF", foreground="#333333", text="Induction days are appointed by the gym manager, contact below:", font=('Poppins', 30), wraplength=600)
        I_ScriptLabel.place(x=215, y=150, width=600, height=100)

        I_Teacher_Button = ttk.Button(I_window, style="Menu2.TButton", text="Send message", command=lambda: Funcs.sendemail(teacheremail, ACCID, True))
        I_Teacher_Button.place(x=360, y=250, width=300, height=50)

        I_window.after(60, closewindows, windows)

        I_window.mainloop()

    else:
        I_window.deiconify()

        closewindows(windows)

def openMed(ACCID):
    global SU_window, LG_window, H_window, B_window, C_window, I_window, M_window
    windows = [SU_window, LG_window, H_window, B_window, C_window, I_window, ]
    closewindows(windows)
    # This function opens the medical certificate window GUI or, if already stored, shows it. It then hides the previous window to give an idea of continuity
    if M_window == None:
        M_window = tk.Toplevel(LG_window)
        SpawnX = int((M_window.winfo_screenwidth() / 2) - (900 / 2))
        SpawnY = int((M_window.winfo_screenheight() / 2) - (430 / 2))
        M_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
        M_window.title("Certificate")
        M_window.resizable(width=False, height=False)

        M_TopLabel = Label(M_window, background="#eb5841", foreground="#333333", text="SLS gym - Certificate ", font=('Poppins', 38))
        M_TopLabel.place(x=150, y=0, width=750, height=75)

        M_Home_Button = ttk.Button(M_window, style="ToolB.TButton", text="Home", command=lambda: openHome(ACCID))
        M_Home_Button.place(x=0, y=0, width=150, height=75)

        M_Induction_Button = ttk.Button(M_window, style="ToolB.TButton", text="Induction", command=lambda: openInduction(ACCID))
        M_Induction_Button.place(x=0, y=75, width=150, height=75)

        M_Med_Button = ttk.Button(M_window, style="ToolBA.TButton", text="Certificate")
        M_Med_Button.place(x=0, y=150, width=150, height=75)

        M_TMT_Button = ttk.Button(M_window, style="ToolB.TButton", text="Bookings", command=lambda: openBook(ACCID))
        M_TMT_Button.place(x=0, y=225, width=150, height=75)

        M_Contact_Button = ttk.Button(M_window, style="ToolB.TButton", text="Contact", command=lambda: openContact(ACCID))
        M_Contact_Button.place(x=0, y=300, width=150, height=75)

        M_Exit_Button = ttk.Button(M_window, style="ToolB.TButton", text="Exit", command=lambda: QuitApp())
        M_Exit_Button.place(x=0, y=375, width=150, height=75)

        M_ScriptLabel = Label(M_window, background="#FFFFFF", foreground="#333333", text="Select new certificate below:", wraplength=600, font=('Poppins', 30))
        M_ScriptLabel.place(x=215, y=100, width=600, height=50)

        M_Select_Button = ttk.Button(M_window, style="Menu2.TButton", text="Select file", command=lambda: Funcs.select_file(M_Select_Button))
        M_Select_Button.place(x=360, y=150, width=300, height=50)

        M_MedTB = Entry(M_window, background="#FFFFFF", foreground="#333333",font=("Poppins",30),justify='center')
        M_MedTB.place(x=360, y=275, width=300, height=50)

        M_DateLabel = Label(M_window, background="#FFFFFF", foreground="#333333", text="Insert certificare expiry date:", wraplength=600, font=('Poppins', 30))
        M_DateLabel.place(x=215, y=225, width=600, height=50)

        M_Upload_Button = ttk.Button(M_window, style="Menu2.TButton", text="Upload Certificate", command=lambda: Funcs.upload_file(M_MedTB, ACCID))
        M_Upload_Button.place(x=360, y=350, width=300, height=50)

        M_window.after(60, closewindows, windows)

        M_window.mainloop()

    else:
        M_window.deiconify()

        closewindows(windows)


# Startup

if __name__ == "__main__":
    Funcs.load_creds()
    Funcs.initialize_connection()
    openlogin()
    atexit.register(Funcs.close_connection)
    #Wilco, here the magic begins and the app starts, it loads creds for connecting, it connects, and it opens. It also tries to close the connection on closure but only if the app is closed properly
