import tkinter as tk
from tkinter import ttk

def TTBTN_click:
S_window = tk.Tk()
S_window.title("Student Attendance")
S_window.geometry("400x400")
S_window.resizable(width=False, height=False)

# Create a frame for the Treeview and the scrollbar
frame = tk.Frame(S_window)
frame.pack(fill=tk.BOTH, expand=True)
tree = ttk.Treeview(frame, columns=("Student", "Present"), show="headings")
tree.heading("Student", text="Student")
tree.heading("Present", text="Present")
tree.column("Student", width=200, anchor=tk.W)
tree.column("Present", width=100, anchor=tk.CENTER)

vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(fill=tk.BOTH, expand=True)


students = S_in_period(i,o)


for student in students:
    tree.insert("", "end", values=(student, "Mark Present"))

# Function to handle click events on the treeview
def on_click(event):
    # Get the clicked item
    region = tree.identify_region(event.x, event.y)
    item = tree.identify_row(event.y)
    column = tree.identify_column(event.x)

    if region == "cell":  # Ensure the click is inside a cell
        # Get item text and column clicked
        item_data = tree.item(item)
        student_name = item_data["values"][0]  # "Student" column value
        present_status = item_data["values"][1]  # "Present" column value

        if column == "#1":  # First column ("Student") clicked
            print(f"Student '{student_name}' clicked!")
        elif column == "#2":  # Second column ("Present") clicked
            # Simulate marking the student as present
            print(f"Marking {student_name} as present.")
            tree.item(item, values=(student_name, "Present"))

# Bind the left-click event on the Treeview
tree.bind("<Button-1>", on_click)

# Run the main Tkinter event loop
S_window.mainloop()
