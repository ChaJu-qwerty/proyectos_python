import random


def jugar():
    usuario = input('escoge uno: "pi" para piedra, "pa" para papel, "ti" para tijera.\n').lower() #\n  significa el fin de una linea visible o en la presentacion 
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return 'empate'
    
    if gano_el_jugador(usuario, computadora): #llamando a la funcion
        return 'ganaste :D'

    return 'perdiste'


def gano_el_jugador(jugador, oponente): #definicion de la funcion 
    # retornar el valor true si gano el jugador
    # piedra gana a tijera (pi > ti)
    # tijera gana a papel (ti > pa)
    # papel gana a piedra (pa > pi)

    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())