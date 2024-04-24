#Admin Dashboard
from tkinter import*
from tkinter import messagebox,PhotoImage
from PIL import Image,ImageTk 
from course import CourseClass
from student import StudentClass
from result import ResultClass
from ViewResult import ViewClass
import sqlite3 
import os
class ResultManagementSystem:
    def __init__(self,home):
        self.home=home
        self.home.title("Student Result Management System")
        self.home.geometry("1600x790+0+0")
        self.home.config(bg="white")

        #Importing image logo (icons)
        
        original_logo = Image.open("image/School Online Education Logo.png")
        resized_logo = original_logo.resize((100, 100), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(resized_logo)
        
        #Title of project
        title=Label(self.home,text="Student Result Management",padx=10,compound=LEFT,image=self.logo_dash, font=("Comic Sans MS",20,"bold"),bg="#FF6E6E",fg="white").place(x=0,y=0,relwidth=1,height=50)



        #    Content_window
        self.bg_img = Image.open("image/e-learning-elements-laptop-used-classes.jpg.webp")
        self.bg_img = self.bg_img.resize((920,350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.home, image=self.bg_img).place(x=300, y = 200,width=900,height= 400)


        # Menu 
        Frame = LabelFrame(self.home,text="Menu",font=("times new roman",15,"bold"),bg="white")
        Frame.place(x=225,y=70,width=1125,height=80)

        #SubMenu
        button_Course=Button(Frame,text="Course",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)

        button_Student=Button(Frame,text="Student",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)

        button_Result=Button(Frame,text="Result",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)

        button_View=Button(Frame,text="View Student Result",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add_view).place(x=680,y=5,width=200,height=40)

        button_Logout=Button(Frame,text="Logout",font=("ties new roman",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)


        # footer
        footer = Label(self.home, text="SRMS-Student Result Management System\nContact Nikola for Technical Issue: 01234567889",font=("times new roman",12),bg="#262626", fg="white").pack(side=BOTTOM,fill=X)
    #Adding Sub-Menus for Functioning 
    def add_course(self):
        self.window1=Toplevel(self.home)
        self.obj1=CourseClass(self.window1)

    def add_student(self):
        self.window1=Toplevel(self.home)
        self.obj1=StudentClass(self.window1)
    
    def add_result(self):
        self.window1=Toplevel(self.home)
        self.obj1=ResultClass(self.window1)
    
    def add_view(self):
        self.window1=Toplevel(self.home)
        self.obj1=ViewClass(self.window1)

#Functioning of Exit and Logout Button
    def logout(self):
        op=messagebox.askyesno("Confirm Again","Do You really Want to Logout ?",parent=self.home)
        if op==True:
            self.home.destroy()
            os.system("Python Login.py")


if __name__=="__main__":
    home=Tk()
    obj=ResultManagementSystem(home)
    home.mainloop()