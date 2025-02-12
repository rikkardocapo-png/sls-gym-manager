
from tkinter import *
import tkinter as tk
from tkinter import ttk
import atexit

L_window = tk.Tk()
SpawnX = int((L_window.winfo_screenwidth() / 2) - (900 / 2))
SpawnY = int((L_window.winfo_screenheight() / 2) - (430 / 2))
L_window.geometry(f"900x450+{SpawnX}+{SpawnY}")
L_window.title("Bookings")
L_window.resizable(width=False, height=False)

B_TopLabel = Label(L_window, background="#eb5841", font=('Poppins', 38), foreground="#333333", justify="center",text="Loading...")
B_TopLabel.place(x=0, y=165, width=900, height=100)
L_window.mainloop()