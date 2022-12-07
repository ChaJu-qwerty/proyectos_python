import time

def esperate_tantito(tiempo):
    time.sleep(tiempo)
    
print('===================')
print(' bienvenido(a) :D ')
print('===================')
esperate_tantito(.5)
print('hoy vamos a hacer algo sencillo\nhoy vamos a checar si un numero es par o impar')

numero = int(input('probemoslo, dame un numero: '))

if numero % 2 == 0:
    print('el numero es par :)')
else:
    print('el numero es impar :O')
