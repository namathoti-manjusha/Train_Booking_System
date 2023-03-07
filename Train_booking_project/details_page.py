from tkinter import *
import tkinter as tktt
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from pymongo import MongoClient
from tickets_compare import Booktrain

class details():
    def validate_details(self,name,tno,dt,src,dst,tkts):
        self.name=name
        self.tno=tno
        self.dt=dt
        self.src=src
        self.dst=dst
        self.tkts=tkts
        cl = MongoClient(
            "mongodb+srv://josetellis2018:dHmjZHB5MZgPsH0f@cluster0.ghrj9wz.mongodb.net/?retryWrites=true&w=majority")
        db = cl['hcl_data']
        col = db['tkt_book']
        col.insert_one({"Name":self.name,"train no":self.tno,"date":self.dt,"source":self.src,"destination":self.dst,"Tickets":self.tkts})

        obj=Booktrain()
        obj.update_tkt(tkts,tno)
    def details_func(self):
        base=tktt.Tk()
        base.geometry('500x500')

        labl_0 = Label(base, text="WELCOME TO TRAIN BOOKING", width=40, font=("bold", 15), fg="brown")
        labl_0.place(x=0, y=10)

        labl_01 = Label(base, text="Name", width=20, font=("bold", 10))
        labl_01.place(x=2, y=80)
        self.name = tktt.StringVar()

        entry_1 = Entry(base, textvariable=self.name)
        entry_1.place(x=130, y=80)

        labl_1 = Label(base, text="Train no", width=20, font=("bold", 10))
        labl_1.place(x=2, y=120)
        self.tno = tktt.IntVar()

        entry_01 = Entry(base, textvariable=self.tno)
        entry_01.place(x=130, y=120)

        label_2=Label(base,text="Select a date")
        label_2.place(x=50, y=160)
        self.dt=tktt.StringVar()

        entry_04 = DateEntry(base, width=12,background='darkblue',foreground='white',borderwidth=2,textvariable=self.dt)
        entry_04.place(x=130, y=160)

        labl_1 = Label(base, text="Source", width=20, font=("bold", 10))
        labl_1.place(x=10, y=200)
        self.src = tktt.StringVar()

        options=["vijayawada","hyderabad","bangalore","chennai"]

        combo_01 = Combobox(base, values=options,textvariable=self.src)
        combo_01.place(x=130, y=200)
        #combo_01.current(0)

        labl_2 = Label(base, text="Destination", width=20, font=("bold", 10))
        labl_2.place(x=4, y=240)
        self.dst = tktt.StringVar()

        combo_02 = Combobox(base, values=options,textvariable=self.dst)
        combo_02.place(x=130, y=240)

        labl_4 = Label(base, text="No of Tickets", width=20, font=("bold", 10))
        labl_4.place(x=0, y=280)
        self.tkts = tktt.IntVar()

        entry_04 = Entry(base, textvariable=self.tkts)
        entry_04.place(x=130, y=280)

        Button(base, text='Submit', width=10, bg='brown', fg='white',command=lambda :self.validate_details(self.name.get(),self.tno.get(),self.dt.get(),self.src.get(),self.dst.get(),self.tkts.get())).place(x=120, y=320)
        base.mainloop()

obj=details()
obj.details_func()