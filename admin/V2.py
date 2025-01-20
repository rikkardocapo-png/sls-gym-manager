from tkinter import ttk
from tkinter import *
import V2_Libs as Funcs

style=None
B_window=None


# Main window subroutine

def setup_styles():
    global style
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Menu.TButton', background='#FFFFFF', foreground='#333333', padding=5, font=('Times', 20))
    style.map('Menu.TButton',
              background=[('active', '#8a8a8a')])

    style.configure('Menu2.TButton', background='#eb5841', foreground='#333333', padding=5, font=('Times', 15))
    style.map('Menu2.TButton',
              background=[('active', '#8a8a8a')])

    style.configure('ToolBA.TButton', background='#001b5e', foreground='#ebecf0', padding=5)
    style.map('ToolBA.TButton',
              background=[('active', '#2b4e94')])

    style.configure('ToolB.TButton', background='#4277fc', foreground='#000000', padding=5)
    style.map('ToolB.TButton',
              background=[('active', '#88affc')])

    style.configure('Red.TButton', background='red', foreground='#000000', padding=5)
    style.map('Red.TButton',
              background=[('active', '#f57373')])

    style.configure('Green.TButton', background='green', foreground='#000000', padding=5)
    style.map('Green.TButton',
              background=[('active', '#3cab59')])

    style.configure('Yellow.TButton', background='yellow', foreground='#000000', padding=5)
    style.map('Yellow.TButton',
              background=[('active', '#ebe698')])

    style.configure('Purple.TButton', background='purple', foreground='#000000', padding=5)
    style.map('Purple.TButton',
              background=[('active', '#9c59b5')])

def openMain():
    global buttonlist,B_window
    B_window = Tk()
    setup_styles()
    SpawnX = int((B_window.winfo_screenwidth() / 2)-(900/2))
    SpawnY = int((B_window.winfo_screenheight() / 2)-(430/2))
    B_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
    B_window.title("HOME")
    B_window.resizable(width=False, height=False)

    TopLabel = Label(B_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",text="SLS gym - Bookings")
    TopLabel.place(x=0 , y=0, width=900, height=75)

    Exit_Button = ttk.Button(B_window, style="Menu.TButton",text="Exit",  command=lambda: exit())
    Exit_Button.place(x=0, y=375, width=100, height=75)

    List_Button = ttk.Button(B_window, style="Menu.TButton",text="Users", command=lambda: Funcs.AllStudentList(B_window))
    List_Button.place(x=800, y=375, width=100, height=75)

    Rbutton = ttk.Button(B_window, text="Refresh", style="Menu2.TButton", command=lambda:Funcs.refresh(QuitApp(),openMain()))
    Rbutton.place(x=(150), y=(100), width=75, height=50)

    Times=[" 14:00-15:00", "15:00- 16:00", "16:00-16:30", "16:45-17:15","17:15-18:00"]

    for i in range(7):

        TTLabel1 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",text=Funcs.getday(i))
        TTLabel1.place(x=(i*75+225),y=(100),width=75,height=50)
        if Funcs.isweekend(str(Funcs.getday(i))):

            for o in range(5):
                if i == 0:
                    TTLabel2 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",
                                     text=Times[o])
                    TTLabel2.place(x=(150), y=(o*50+150), width=75, height=50)

                TTbutton = ttk.Button(B_window, text=Funcs.getTTstatus(i,o)[0], style=Funcs.getTTstatus(i,o)[1])
                TTbutton.place(x=(i*75+225),y=(o*50+150),width=75,height=50)
                TTbutton.configure(command=lambda i=i, o=o: Funcs.TTBTN_press(i, o, B_window))

        else:
            for o in range(5):
                if i == 0:
                    TTLabel2 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",text=Times[o])
                    TTLabel2.place(x=(150), y=(o * 50 + 150), width=75, height=50)

                WElabel = Label(B_window, bg="grey")
                WElabel.place(x=(i * 75 + 225), y=(o * 50 + 150), width=75, height=50)



    B_window.mainloop()

def QuitApp():
    global B_window
    B_window.destroy()


openMain()


