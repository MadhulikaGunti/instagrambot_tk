import tkinter as tk
from tkinter import messagebox

def test_gui():
    root = tk.Tk()
    root.title("Instagram Bot")
    root.geometry("300x200")

    tk.Label(root, text="Enter Username:").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Enter Password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def test_message():
        messagebox.showinfo("Info", "This is a test message!")

    tk.Button(root, text="Test", command=test_message).pack()

    root.mainloop()

test_gui()
