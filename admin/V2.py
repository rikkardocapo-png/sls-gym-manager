import tkmacosx as btnx
from tkinter import *
import V2_Libs as Funcs

# Main window subroutine

def openMain():


    B_window = Tk()
    SpawnX = int((B_window.winfo_screenwidth() / 2)-(900/2))
    SpawnY = int((B_window.winfo_screenheight() / 2)-(430/2))
    B_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
    B_window.title("HOME")
    B_window.resizable(width=False, height=False)

    TopLabel = Label(B_window, bg="#eb5841", font=('Times', 38), fg="#333333", justify="center",
                       text="SLS gym - Bookings")
    TopLabel.place(x=0 , y=0, width=900, height=75)

    Exit_Button = btnx.Button(B_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center",
                            text="Exit",  command=lambda: Funcs.closewindow(B_window))
    Exit_Button.place(x=0, y=375, width=100, height=75)

    List_Button = btnx.Button(B_window, bg="#efefef", font=('Times', 10), fg="#000000", justify="center",
                              text="Users", command=lambda: Funcs.AllStudentList())
    List_Button.place(x=800, y=375, width=100, height=75)

    Times=[" 14:00-15:00", "15:00- 16:00", "16:00-16:30", "16:45-17:15","17:15-18:00"]

    for i in range(7):

        TTLabel1 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",
                       text=Funcs.getday(i))
        TTLabel1.place(x=(i*75+225),y=(100),width=75,height=50)
        if Funcs.isweekend(str(Funcs.getday(i))):

            for o in range(5):
                if i == 0:
                    TTLabel2 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",
                                     text=Times[o])
                    TTLabel2.place(x=(150), y=(o*50+150), width=75, height=50)

                TTbutton = btnx.Button(B_window, text=Funcs.getTTstatus(i,o)[0], bg=Funcs.getTTstatus(i,o)[1])
                TTbutton.place(x=(i*75+225),y=(o*50+150),width=75,height=50)
                TTbutton.configure(command=lambda i=i, o=o: Funcs.TTBTN_press(i, o))

        else:
            for o in range(5):
                if i == 0:
                    TTLabel2 = Label(B_window, bg="#eb5841", font=('Times', 10), fg="#333333", justify="center",
                                     text=Times[o])
                    TTLabel2.place(x=(150), y=(o * 50 + 150), width=75, height=50)

                WElabel = Label(B_window, bg="grey")
                WElabel.place(x=(i * 75 + 225), y=(o * 50 + 150), width=75, height=50)



    B_window.mainloop()


openMain()


