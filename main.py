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
    