#Course Module
from tkinter import*
from PIL import Image,ImageTk  
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,home):
        self.home=home
        self.home.title("Student Result Management System")
        self.home.geometry("1600x900+0+0")
        self.home.config(bg="white")
        self.home.focus_force()

    #Title of Course
        title=Label(self.home,text="Manage Course",font=("times new roman",20,"bold"),bg="#CC3366",fg="white").place(x=0,y=0,relwidth=1,height=40)
    #Variables
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

    #Categories of Courses
        courseName = Label(self.home,text="Course Name",font=("times new roman",15,"bold"),bg="white").place(x=550,y=100)
        description = Label(self.home,text="Description",font=("times new roman",15,"bold"),bg="white").place(x=550,y=150)

    #Entry Fields
        self.courseName1 = Entry(self.home,textvariable=self.var_course,font=("times new roman",15,"bold"),bg="lightyellow")
        self.courseName1.place(x=700,y=100,width=200)
        self.description1 = Text(self.home,font=("times new roman",15,"bold"),bg="lightyellow")
        self.description1.place(x=700,y=150,width=500,height=150)

    # Buttons
        self.add_btn=Button(self.home,text="Save",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add)
        self.add_btn.place(x=570,y=400,width=120,height=50)
        self.delete_btn=Button(self.home,text="Delete",font=("times new roman",15,"bold"),bg="grey",fg="white",cursor="hand2",command=self.delete)
        self.delete_btn.place(x=730,y=400,width=120,height=50)
        self.clear_btn=Button(self.home,text="Clear",font=("times new roman",15,"bold"),bg="orange",fg="white",cursor="hand2",command=self.clear)
        self.clear_btn.place(x=900,y=400,width=120,height=50)

        
#--------------database----------------------------------
#Adding name,duration, discription and showing pop messages on pc accordint to that

    def clear(self):
        self.var_course.set("")
        self.description1.delete('1.0',END)
        self.courseName1.config(state=NORMAL)

    def delete(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.home)
            else:
                cur.execute("Select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error, Select The Course From the List first",parent=self.home)
                else:
                    p=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.home)
                    if p==True:
                        cur.execute("Delete from course where name=? ",(self.var_course.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","Course deleted Successfully",parent=self.home)
                        self.clear() #We are calling clear because we declare show in to that
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

# Adding Details and Saving
    def add(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.home)
            else:
                cur.execute("Select * from course where name=?",(self.var_course.get(),)) #Due to tupple we added , at last
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error, Course name already Present",parent=self.home)
                else:
                    cur.execute("Insert into course (name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.description1.get("1.0",END)
                    ) )
                    conn.commit()
                    messagebox.showinfo("Great","Course Added Successfully",parent=self.home)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



if __name__=="__main__":
    home=Tk()
    obj=CourseClass(home)
    home.mainloop()