import turtle
import time
import random

posponer = 0.1

#config ventana
wn = turtle.Screen()
wn.title('Snake game')
wn.bgcolor('black')
wn.setup(width= 600, height=600)
wn.tracer(0)

#cabeza serpiente
cabeza = turtle.Turtle() #el Turtle es un objeto especifico
cabeza.speed(0)
cabeza.shape('square') #20 x 20
cabeza.color('white')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop' #el programa esperara hasta que yo le indique a donde avanzar

#comida
comida = turtle.Turtle() 
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(0,110)

#segmentos / cuerpo de la serpiente 
segmentos = []

#funciones
def arriba():
   cabeza.direction = 'up'
def abajo():
   cabeza.direction = 'down'
def izquierda():
   cabeza.direction = 'left'
def derecha():
   cabeza.direction = 'right'

def mov():
    if cabeza.direction == 'up':
       y = cabeza.ycor()
       cabeza.sety(y + 13)
    if cabeza.direction == 'down':
       y = cabeza.ycor()
       cabeza.sety(y - 13)
    if cabeza.direction == 'left':
       x = cabeza.xcor()
       cabeza.setx(x - 13)
    if cabeza.direction == 'right':
       x = cabeza.xcor()
       cabeza.setx(x + 13)

#teclado
wn.listen()
wn.onkeypress(arriba, 'Up') 
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')

while True: 
    wn.update()  # bucle para que funcione el juego
   
    if cabeza.distance(comida) < 20:
      x = random.randint(-280,280)
      y = random.randint(-280,280)
      comida.goto(x,y)
      

    mov()
    time.sleep(posponer)