import tkinter as tk
from tkinter import *
from subprocess import call
def clickabout():
    call(["python","login_page.py"])
def clickregister():
    call(["python", "registration_page.py"])
top=tk.Tk()

top.config(bg="Pink")
top.geometry("500x600")
top.title("RAILWAY TICKET RESERVATION")
def close():
    top.destroy()
    top.quit()
#canvas = Canvas(top,width=1000,height=750,bg='pink')
#canvas.create_text(250,50,text="TICKET BOOKING",font=('Helvetica 15 bold'))
#canvas.pack()
# obj=login()
# obj1=registration()
label=Label(top,text="TICKET BOOKING",bg="pink",font=('Helvetica 20 bold')).place(x=150,y=0)
butt_1=Button(top,text="Login",width=7,bg="white",command=clickabout).place(x=220,y=60)
butt_2=Button(top,text="Register",width=7,bg="white",command=clickregister).place(x=220,y=100)
butt_3=Button(top,text="Exit",width=7,bg="white",command=close).place(x=220,y=140)

label=Label(top,text="TRAIN INFORMATION",bg="pink",font=('Helvetica 15 bold')).place(x=150,y=200)
label=Label(top,text="Train no:       Train Name:          Source:    Destination:",bg="pink",font=('Helvetica 10 bold')).place(x=100,y=230)


label=Label(top,text="  12711 \t\t Pinakini SF Express \t Vijayawada \t Chennai",bg="pink",font=('Helvetica 7')).place(x=100,y=260)
label=Label(top,text="  12616 \t\t Grand Trank SF Express \t Delhi \t\t Chennai",bg="pink",font=('Helvetica 7')).place(x=100,y=275)
label=Label(top,text="  12925\t\t Paschim SF Express \t Mumbai \t\t New Delhi",bg="pink",font=('Helvetica 7')).place(x=100,y=290)
label=Label(top,text="  12627 \t\t Karnataka Express \t Bangaluru \t New Delhi",bg="pink",font=('Helvetica 7')).place(x=100,y=305)
label=Label(top,text="  18047 \t\t Amaravati Express \t Vijayawada \t Vasco-da-Gama",bg="pink",font=('Helvetica 7')).place(x=100,y=320)
top.mainloop()

