from tkinter import *
from tkinter import Label
import time


raiz = Tk()
nom = Entry(width=30,borderwidth=3).grid(row=0,column=1,padx=10)
ape = Entry(width=30,borderwidth=3).grid(row=1,column=1,padx=10)

texNOM = Label(text='NOMBRE').grid(row=0,column=0)
texAPE = Label(text='APELLIDO').grid(row=1,column=0)

Button(text= 'ACEPTAR',width=40,command=lambda:[raiz.destroy()]).grid(row=5,column=1,padx=10)

raiz.mainloop()