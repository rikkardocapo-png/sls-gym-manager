import tkinter
from tkinter import ttk


root = tkinter.Tk()
root.geometry("400x400")

style = ttk.Style()

style.theme_use("clam")
style.configure("TButton",
                foreground="#ebecf0",
                background="#001b5e",
                font=('Times', 12),)

print("loading styles 100%")
print(style)


btn = ttk.Button(style="TButton",text="efhkfbkwfbwfjbkewf")
btn.place(x=40,y=30,height=50,width=100)

root.mainloop()



