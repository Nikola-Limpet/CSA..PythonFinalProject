from os import name
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import re  # Added for email validation
from datetime import datetime  # Added for date validation

class StudentClass:
    def __init__(self, home):
        self.home = home
        self.home.title("Student Result Management System")
        self.home.geometry("1600x900+0+0")
        self.home.config(bg="white")
        self.home.focus_force()

        # Title of Course
        title = Label(self.home, text="Manage Student Details", font=("times new roman", 20, "bold"), bg="#CC3366", fg="white").place(x=0, y=0, relwidth=1, height=40)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_adm_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        

        # Categories of student details 1 side
        rollno = Label(self.home, text="Roll No.", font=("times new roman", 15, "bold"), bg="white").place(x=470, y=60)
        name = Label(self.home, text="Name", font=("times new roman", 15, "bold"), bg="white").place(x=470, y=100)
        email = Label(self.home, text="Email", font=("times new roman", 15, "bold"), bg="white").place(x=470, y=140)
        gender = Label(self.home, text="Gender", font=("times new roman", 15, "bold"), bg="white").place(x=470, y=180)

        state = Label(self.home, text="State", font=("times new roman", 15, "bold"), bg="white").place(x=470, y=220)
        self.state1 = Entry(self.home, textvariable=self.var_state, font=("times new roman", 15, "bold"), bg="lightyellow")
        self.state1.place(x=560, y=220, width=150)

        city = Label(self.home, text="City", font=("times new roman", 15, "bold"), bg="white").place(x=730, y=220)
        self.city1 = Entry(self.home, textvariable=self.var_city, font=("times new roman", 15, "bold"), bg="lightyellow")
        self.city1.place(x=800, y=220, width=110)

        # pin = Label(self.home, text="Pin", font=("times new roman", 15, "bold"), bg="white").place(x=920, y=220)
        # self.pin1 = Entry(self.home, textvariable=self.var_pin, font=("times new roman", 15, "bold"), bg="lightyellow")
        # self.pin1.place(x=980, y=220, width=120)

        address = Label(self.home, text="Address", font=("times new roman", 15, "bold"), bg="white").place(x=470, y=260)

        # Entry Fields 1
        self.rollno1 = Entry(self.home, textvariable=self.var_roll, font=("times new roman", 15, "bold"), bg="lightyellow")
        self.rollno1.place(x=560, y=60, width=200)

        name1 = Entry(self.home, textvariable=self.var_name, font=("times new roman", 15, "bold"), bg="lightyellow").place(x=560, y=100, width=200)
        email1 = Entry(self.home, textvariable=self.var_email, font=("times new roman", 15, "bold"), bg="lightyellow").place(x=560, y=140, width=200)

        self.gender1 = ttk.Combobox(self.home, textvariable=self.var_gender, values=("Select", "Male", "Female"), font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
        self.gender1.place(x=560, y=180, width=200)
        self.gender1.current(0)

        # Address
        self.address = Text(self.home, font=("times new roman", 15, "bold"), bg="lightyellow")
        self.address.place(x=560, y=260, width=540, height=100)

        # Categories of student details 2 side
        dob = Label(self.home, text="D.O.B", font=("times new roman", 15, "bold"), bg="white").place(x=800, y=60)
        contact = Label(self.home, text="Contact", font=("times new roman", 15, "bold"), bg="white").place(x=800, y=100)
        admission = Label(self.home, text="Admission", font=("times new roman", 15, "bold"), bg="white").place(x=800, y=140)
        course = Label(self.home, text="Course", font=("times new roman", 15, "bold"), bg="white").place(x=800, y=180)

        # Entry Fields 2
        self.course_list = []
        # Function call to update list
        self.fetch_course()

        self.dob1 = Entry(self.home, textvariable=self.var_dob, font=("times new roman", 15, "bold"), bg="lightyellow")
        self.dob1.place(x=900, y=60, width=200)

        contact1 = Entry(self.home, textvariable=self.var_contact, font=("times new roman", 15, "bold"), bg="lightyellow").place(x=900, y=100, width=200)
        admission1 = Entry(self.home, textvariable=self.var_adm_date, font=("times new roman", 15, "bold"), bg="lightyellow").place(x=900, y=140, width=200)

        self.course1 = ttk.Combobox(self.home, textvariable=self.var_course, values=self.course_list, font=("times new roman", 15, "bold"), state="readonly", justify=CENTER)
        self.course1.place(x=900, y=180, width=200)
        self.course1.set("Select")

        # Buttons
        self.add_btn = Button(self.home, text="Save", font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2", command=self.add)
        self.add_btn.place(x=560, y=400, width=120, height=50)
        self.update_btn = Button(self.home, text="Update", font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2", command=self.update)
        self.update_btn.place(x=700, y=400, width=120, height=50)
        self.delete_btn = Button(self.home, text="Delete", font=("times new roman", 15, "bold"), bg="grey", fg="white", cursor="hand2", command=self.delete)
        self.delete_btn.place(x=840, y=400, width=120, height=50)
        self.clear_btn = Button(self.home, text="Clear", font=("times new roman", 15, "bold"), bg="orange", fg="white", cursor="hand2", command=self.clear)
        self.clear_btn.place(x=980, y=400, width=120, height=50)

# --------------database----------------------------------
# Adding name, duration, description, and showing pop messages on PC according to that

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_adm_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        
        self.address.delete("1.0", END)
        self.rollno1.config(state=NORMAL)

    def delete(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No should be required", parent=self.home)
            else:
                cur.execute("Select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error, Select The Student From the List first", parent=self.home)
                else:
                    p = messagebox.askyesno("Confirm", "Do you really want to delete", parent=self.home)
                    if p == True:
                        cur.execute("Delete from student where roll=? ", (self.var_roll.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete", "Student deleted Successfully", parent=self.home)
                        self.clear()  # We are calling clear because we declare show in to that
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Adding Details and Saving
    def add(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            roll = self.var_roll.get()
            name = self.var_name.get()
            email = self.var_email.get()
            gender = self.var_gender.get()
            dob = self.var_dob.get()
            contact = self.var_contact.get()
            adm_date = self.var_adm_date.get()
            course = self.var_course.get()
            state = self.var_state.get()
            city = self.var_city.get()
            
            address = self.address.get("1.0", END)
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Course Name should be required", parent = self.home)
            else:
                cur.execute("select * from student where roll=?" , (self.var_roll.get(), ))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Roll Name already present", parent = self.home)
                else:
                            cur.execute("INSERT INTO student (roll, name, email, gender, dob, contact, admission, course, state, city, address) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (
                                roll, name, email, gender, dob, contact, adm_date, course, state, city, address))
                            conn.commit()
                            messagebox.showinfo("Success", "Student Added Successfully", parent=self.home)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # Updating Details
    def update(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No should be required", parent=self.home)
            else:
                cur.execute("Select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Student From List", parent=self.home)
                else:
                    cur.execute("Update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where  roll=? ", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adm_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.address.get("1.0", END),
                        self.var_roll.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Great", "Student Update Successfully", parent=self.home)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_course(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            cur.execute("Select name from course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

if __name__ == "__main__":
    home = Tk()
    obj = StudentClass(home)
    home.mainloop()
