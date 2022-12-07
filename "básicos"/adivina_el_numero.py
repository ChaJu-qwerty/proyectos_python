import random


def adivina_el_numero(x):
    print('===================')
    print(' bienvenido(a) :D ')
    print('===================')
    print('tu meta es adivinar el numero generado por la computadora')

    numero_aleatorio = random.randint(1, x) #numero aleatorio entre 1 y x

    prediccion = 0 #se comienza en 0 para que no coinsida con el numero aleatorio

    while prediccion != numero_aleatorio:
        #el usuario ingresa un numero
        prediccion = int(input(f'adivina un numero entre 1 y {x}: '))

        if prediccion < numero_aleatorio:
            print('Intentalo otra vez. Este numero es muy pequeño')
        elif prediccion > numero_aleatorio:
            print('Intentalo otra vez. Este numero es muy grande')
    
    print(f'felicitaciones adivinaste el numero {numero_aleatorio} correctamente :D')


adivina_el_numero(10)