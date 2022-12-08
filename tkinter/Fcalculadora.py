import tkinter as tk
from tkinter import ttk, Frame, ttk, Entry, END, Label, Button
from math import *


atras = tk.Tk()
atras.title("calculadora fake")
atras.config(background='#164219232')

#adv = Label(atras, text='solo funciona con dos numeros').pack()

e=Entry(width=30,borderwidth=2,font=("Calibri",15))
e.grid(row=1,column=0,columnspan=5,padx=10,pady=20,ipady=5)


    #definir las cosas que voy a hacer
def click(num):
    n=e.get() #es como decirle agarra lo que esta en e
    e.delete(0,END) #El uso de los índices (0, END) equivaldría a seleccionar todo el texto disponible en e
    e.insert(1,str(n)+str(num))

def limpiarT():
    e.delete(0,END)

def limpiarU():
    e.delete(1,END)

def suma():
    num1 = e.get()
    global n1
    global c1
    c1 = 'suma'
    n1 = float(num1)
    e.delete(0,END)

def resta():
    num1 = e.get()
    global n1
    global c1
    c1 = 'resta'
    n1 = float(num1)
    e.delete(0,END)

def dividir():
    num1 = e.get()
    global n1
    global c1
    c1 = 'dividir'
    n1 = float(num1)
    e.delete(0,END)

def multiplicar():
    num1 = e.get()
    global n1
    global c1
    c1 = 'multiplicar'
    n1 = float(num1)
    e.delete(0,END)

def porcentaje():
    num1 = e.get()
    global n1
    global c1
    c1 = 'porcentaje'
    n1 = float(num1)
    e.delete(0,END)

def igual():
    num2=e.get()
    n2=num2
    e.delete(0,END)

    if c1=='suma':
        e.insert(0,float(n1) + float(n2))
    elif c1=='resta':
        e.insert(0,float(n1) - float(n2))
    elif c1=='dividir':
        e.insert(0,float(n1) / float(n2))
    elif c1=='multiplicar':
        e.insert(0,float(n1) * float(n2))
    elif c1=='porcentaje':
        e.insert(0,float(n1) % float(n2))

bAdv=Button(atras,font=10,text='usar solo para cosas muy basicas (dos terminos), por favor y gracias :D',background='white',foreground='red').grid(row=0,column=0,columnspan=5,padx=10,pady=20,ipady=5)

b1=Button(atras,font=10,text='1',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(1)).grid(row=5,column=0)
b2=Button(atras,font=10,text='2',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(2)).grid(row=5,column=1)
b3=Button(atras,font=10,text='3',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(3)).grid(row=5,column=2)
b4=Button(atras,font=10,text='4',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(4)).grid(row=4,column=0)
b5=Button(atras,font=10,text='5',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(5)).grid(row=4,column=1)
b6=Button(atras,font=10,text='6',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(6)).grid(row=4,column=2)
b7=Button(atras,font=10,text='7',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(7)).grid(row=3,column=0)
b8=Button(atras,font=10,text='8',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(8)).grid(row=3,column=1)
b9=Button(atras,font=10,text='9',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(9)).grid(row=3,column=2)
b0=Button(atras,font=10,text='0',padx=50,pady=15,background='gray',foreground='white',command=lambda:click(0)).grid(row=6,column=1)
b=Button(atras,font=10,text='.',padx=50,pady=15,background='gray',foreground='white',command=lambda:click('.')).grid(row=6,column=2)
bIg=Button(atras,font=10,text='=',padx=50,pady=15,background='gray',foreground='white',command=igual).grid(row=6,column=3)
bS=Button(atras,font=10,text='+',padx=50,pady=15,background='gray',foreground='white',command=suma).grid(row=5,column=3)
bR=Button(atras,font=10,text='-',padx=50,pady=15,background='gray',foreground='white',command=resta).grid(row=4,column=3)
bM=Button(atras,font=10,text='*',padx=50,pady=15,background='gray',foreground='white',command=multiplicar).grid(row=3,column=3)
bPor=Button(atras,font=10,text='%',padx=50,pady=15,background='gray',foreground='white',command=porcentaje).grid(row=6,column=0)
bLim=Button(atras,text='CE',font=10,padx=45,pady=15,bg='gray',fg='red',command=limpiarT).grid(row=2,column=2)



atras.mainloop()