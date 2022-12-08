import tkinter as tk
from tkinter import Frame, ttk
import random
#from click import command
import webbrowser


#lo de atras (no se ve, pero creo que devo de ponerlo)
atras = tk.Tk()
atras.title('secreto')
#atras.iconbitmap('pregunta.ico')

#texto
texto1 = tk.Label(atras,text="Quieres ver Hamilton?")
texto1.pack()
texto1.config(bg='#ADD8E6')

#ventana
ventana = tk.Frame()
ventana.pack()
ventana.config(bg='#164219232')
ventana.config(width=600,height=600)

#botonSi
    #link
def link():
    webbrowser.open_new(r"https://www.youtube.com/watch?v=C5_jL9qNkgQ")
stilo1=ttk.Style()
stilo1.configure('BotonnSi.TButton', background='green')
botonSi=ttk.Button(text='si :3',style='BotonnSi.TButton', command=lambda:[link(), atras.destroy()])
botonSi.place(x=180, y=140)

#boton2
    #huida
def huida():
    botonNo.place(x=random.randint(20,570), y=random.randint(20,570))
stilo2=ttk.Style()
stilo2.configure('BotonnNo.TButton', background='red')
botonNo=ttk.Button(text='no >:| ',style='BotonnNo.TButton', command=huida )
botonNo.place(x=300, y=140)


atras.mainloop()