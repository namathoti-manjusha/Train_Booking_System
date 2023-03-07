from tkinter import *
from pymongo import MongoClient
import tkinter as tktt
from tkinter import messagebox
class registration():
    def validate(self,fname,email,gender,age,username,pwd):
        self.fname=fname
        self.email=email
        self.gender=gender
        self.age=age
        self.username=username
        self.pwd=pwd
        cl = MongoClient(
            "mongodb+srv://josetellis2018:dHmjZHB5MZgPsH0f@cluster0.ghrj9wz.mongodb.net/?retryWrites=true&w=majority")
        db = cl['hcl_data']
        col = db['registration']
        col.insert_one({"firstname":self.fname,"email":self.email,"gender":self.gender,"age":self.age,"username":self.username,"password":self.pwd})
        messagebox.showinfo('HCL','User Added Successfully')

    def registartion_func(self):

        base = Tk()
        base.geometry('500x500')
        base.title("Registration Form")

        labl_0 = Label(base, text="Registration form", width=20, font=("bold", 20))
        labl_0.place(x=90, y=53)

        labl_1 = Label(base, text="FullName", width=20, font=("bold", 10))
        labl_1.place(x=80, y=130)
        self.fname=tktt.StringVar()
        entry_1 = Entry(base,textvariable=self.fname)
        entry_1.place(x=240, y=130)

        labl_2 = Label(base, text="Email", width=20, font=("bold", 10))
        labl_2.place(x=68, y=180)
        self.email=tktt.StringVar()
        entry_02 = Entry(base,textvariable=self.email)
        entry_02.place(x=240, y=180)

        labl_3 = Label(base, text="Gender", width=20, font=("bold", 10))
        labl_3.place(x=70, y=230)
        self.gender=tktt.IntVar()
        Radiobutton(base, text="Male", padx=1,variable=self.gender ,value=1).place(x=235, y=230)
        Radiobutton(base, text="Female", padx=5, variable=self.gender , value=2).place(x=300, y=230)

        labl_4 = Label(base, text="Age:", width=20, font=("bold", 10))
        labl_4.place(x=70, y=280)
        self.age=tktt.IntVar()
        entry_02 = Entry(base,textvariable=self.age)
        entry_02.place(x=240, y=280)


        labl_5 = Label(base, text="username", width=20, font=("bold", 10))
        labl_5.place(x=70, y=330)
        self.username=tktt.StringVar()

        entry_03 = Entry(base,textvariable=self.username)
        entry_03.place(x=240, y=330)

        labl_6 = Label(base, text="password", width=20, font=("bold", 10))
        labl_6.place(x=72, y=380)
        self.pwd=tktt.StringVar()

        entry_04 = Entry(base,textvariable=self.pwd)
        entry_04.place(x=240, y=380)
        Button(base, text='Submit', width=20, bg='brown', fg='white',command= lambda :self.validate(self.fname.get(),self.email.get(),self.gender.get(),self.age.get(),self.username.get(),self.pwd.get())).place(x=180, y=420)
        # it will be used for displaying the registration form onto the window
        base.mainloop()

obj=registration()
obj.registartion_func()