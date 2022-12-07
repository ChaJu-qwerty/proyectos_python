#concadenar cadenas de caracteres
import time

print("juguemos a 🎇historias locas🎇")
time.sleep(1.5)
accede = input('quieres jugar? ')
if accede == "no":
    time.sleep(.5)
    print("okey :)")
    time.sleep(2)
    print('hasta la proxima (^人^)')
elif accede == "si":
    time.sleep(.5)
    print('okey :D')
    time.sleep(.5)
    print('empezemos...')
    time.sleep(1.5)
    organizacion = input('dime una organización: ')
    time.sleep(.5)
    emocion = input('dime una emoción: ')
    time.sleep(1)
    print('okey, ya tenemos la historia lista :O')
    time.sleep(.5)
    historia_loca_xd = input('quieres oirla? ')
    if historia_loca_xd == 'no':
        time.sleep(.5)
        print('okey, no te preocupes :(')
        time.sleep(.3)
        print('chao')
    elif historia_loca_xd == "si":
        time.sleep(.5)
        print('okey :D, aqui va')
        # for number in range(1, 4):
        #     print(number)
        time.sleep(1)
        print(f'hoy aprenderemos a cocinar con {organizacion}, estoy muy {emocion} por esto')


#alt + z  para que un renglon largo se ponga en varios renglones sin afectar el codigo ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
