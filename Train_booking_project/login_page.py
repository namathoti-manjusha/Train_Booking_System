import tkinter as tkt
from tkinter import *
from tkinter import messagebox
from functools import partial
from pymongo import MongoClient
from subprocess import call
class login:

    def validateLogin(self,username,password):
         # print("username entered :", username.get())
         # print("password entered :", password.get())
         self.username=username
         self.password=password
         cl = MongoClient(
             "mongodb+srv://josetellis2018:dHmjZHB5MZgPsH0f@cluster0.ghrj9wz.mongodb.net/?retryWrites=true&w=majority")
         db = cl['hcl_data']
         col = db['registration']

         user = col.find_one({"username": self.username, "password": password})
         if user:
             #messagebox.showinfo("login","Login successful")
             call(["python","details_page.py"])
         else:
             call(["python","registration_page.py"])


    #window
    def login_func(self):
        tk=tkt.Tk()

        tk.geometry('400x150')
        tk.title('Login Form')
        # username label and text entry box
        usernameLabel=Label(tk,text="User Name").grid(row=0, column=0)
        self.username=tkt.StringVar()
        usernameEntry=Entry(tk,textvariable=self.username).grid(row=0, column=1)
        # psw label and psw entry box
        pwdLabel=Label(tk,text="Password").grid(row=1, column=0)
        self.pwd=tkt.StringVar()
        pwdEntry=Entry(tk,textvariable=self.pwd,show='*').grid(row=1, column=1)
        # ob2=login()
        validate_login=partial(self.validateLogin,self.username,self.pwd)
        #loginbutton
        loginButton=Button(tk,text="Login",command=lambda :self.validateLogin(self.username.get(),self.pwd.get())).grid(row=5,column=1)
        tk.mainloop()
obj=login()
obj.login_func()