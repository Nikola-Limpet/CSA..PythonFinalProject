import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

class Login:
    def __init__(self, home):
        self.home = home
        self.home.title("Login System")
        self.home.geometry("1600x900+0+0")

        # Initialize frames for login and register but only show the login frame initially
        self.init_login_frame()
        self.init_register_frame()
        self.show_login_frame()

    def init_login_frame(self):
        self.frame_login = tk.Frame(self.home, bg="white")
        self.frame_login.place(x=580, y=100, height=550, width=500)
        
        title = tk.Label(self.frame_login, text="User Login", font=("Times New Roman", 25, "bold"), fg="navy blue", bg="light gray")
        title.place(x=150, y=20)

        lbl_user = tk.Label(self.frame_login, text="User Name", font=("Times New Roman", 15, "bold"), fg="black", bg="light gray")
        lbl_user.place(x=45, y=140)
        self.txt_user = tk.Entry(self.frame_login, font=("times new roman", 15), bg="white")
        self.txt_user.place(x=45, y=170, width=400, height=35)

        lbl_pass = tk.Label(self.frame_login, text="Password", font=("Times New Roman", 15, "bold"), fg="black", bg="light gray")
        lbl_pass.place(x=45, y=240)
        self.txt_pass = tk.Entry(self.frame_login, font=("times new roman", 15), bg="white")
        self.txt_pass.place(x=45, y=270, width=400, height=35)

        login_btn = tk.Button(self.frame_login, text="Login", command=self.login_function, bg="navy blue", fg="white", font=("times new roman", 20, "bold"))
        login_btn.place(x=210, y=370, width=100, height=50)

        register_btn = tk.Button(self.frame_login, text="Register", command=self.show_register_frame, bg="navy blue", fg="white", font=("times new roman", 20, "bold"))
        register_btn.place(x=210, y=430, width=100, height=50)

    def init_register_frame(self):
        self.frame_register = tk.Frame(self.home, bg="white")
        self.frame_register.place(x=580, y=100, height=550, width=500)
        self.frame_register.place_forget()  # Start with the register frame hidden

        title = tk.Label(self.frame_register, text="Register", font=("Times New Roman", 25, "bold"), fg="navy blue", bg="light gray")
        title.place(x=150, y=20)

        lbl_user = tk.Label(self.frame_register, text="Username", font=("Times New Roman", 15, "bold"), fg="black", bg="light gray")
        lbl_user.place(x=45, y=140)
        self.txt_new_user = tk.Entry(self.frame_register, font=("times new roman", 15), bg="white")
        self.txt_new_user.place(x=45, y=170, width=400, height=35)

        lbl_pass = tk.Label(self.frame_register, text="Password", font=("Times New Roman", 15, "bold"), fg="black", bg="light gray")
        lbl_pass.place(x=45, y=240)
        self.txt_new_pass = tk.Entry(self.frame_register, font=("times new roman", 15), bg="white")
        self.txt_new_pass.place(x=45, y=270, width=400, height=35)

        save_btn = tk.Button(self.frame_register, text="Save", command=self.save_to_database, bg="navy blue", fg="white", font=("times new roman", 20, "bold"))
        save_btn.place(x=210, y=440, width=100, height=50)

        # Add a back button to return to the login frame
        back_btn = tk.Button(self.frame_register, text="Back", command=self.show_login_frame, bg="gray", fg="white", font=("times new roman", 20, "bold"))
        back_btn.place(x=100, y=440, width=100, height=50)

    def show_login_frame(self):
        self.frame_register.place_forget()
        self.frame_login.place(x=580, y=100, height=550, width=500)

    def show_register_frame(self):
        self.frame_login.place_forget()
        self.frame_register.place(x=580, y=100, height=550, width=500)

    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.home)
        elif self.txt_pass.get() == "1234" and self.txt_user.get() == "admin":
            messagebox.showinfo("Success", f"Welcome :- {self.txt_user.get()}", parent=self.home)
            self.home.destroy()
            os.system("python dashboard.py")
        else:
            messagebox.showerror("Error", "Wrong Username or Password", parent=self.home)

    def save_to_database(self):
        conn = sqlite3.connect('ResultManagementSystem.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.txt_new_user.get(), self.txt_new_pass.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User saved to database", parent=self.home)

home = tk.Tk()
obj = Login(home)
home.mainloop()
