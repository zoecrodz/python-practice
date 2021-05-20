def second():
    edad = int(input('ingrese su edad: '))
    contador = 1
    while contador <= edad:
        print(contador)
        contador += 1
second()

def third():
    numero = int(input('ingrese un número entero positivo: '))
    if numero < 1 :
        print('debe ser positivo')
    else :
        contador = 0
        while contador <= numero:
            contador += 1
            if contador % 2 != 0 :
                print(contador)
third()

def fourth():
    numero = int(input('ingrese un número '))
    if numero < 1 :
        print('debe ser positivo')
    else :
        contador = numero
        while contador >= 0:
            print(contador)
            contador -= 1
fourth()

def seventh():
    numero = int(input('ingrese un número '))
    multiplicador = 1
    while multiplicador <= 10:
        print(multiplicador, 'x', numero, '=', multiplicador*numero )
        multiplicador += 1
seventh()

def eighth(): 
    numero = int(input('ingrese un número: '))
    multiplicador = 1
    uno = 1
    tres = 3
    cinco = 5
    siete = 7
    nueve = 9
    while multiplicador <= numero:
        if multiplicador == 1 :
            print(uno)
        elif multiplicador == 2 : 
            print(tres,uno)
        elif multiplicador == 3 :
            print(cinco,tres,uno)
        elif multiplicador == 4 :
            print(siete,cinco,tres,uno)
        elif multiplicador == 5 :
            print(nueve,siete,cinco,tres,uno)
        multiplicador += 1
eighth()

def nineth():
    correcta = 'contraseña'
    contraseña = input('ingrese su contraseña: ')
    if correcta == contraseña :
        print('Bienvenido')
    else : 
        nineth()
nineth()




