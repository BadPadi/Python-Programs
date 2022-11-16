import random

"""Esta función genera numeros aleatorios para nuestra segunda parte del ejercicio,
   creando un for e importando la funcion ramdon entre 1 y 49 y para el reintegro del 0 al 9 .
   Tambien cantidadNumBoleto es una variable que nos permite elegir entre 6 o 7 numeros
   """

def generar_aleatorios(cantidadNumBoleto):
    boleto = list()
    for i in range(cantidadNumBoleto):
        while True:
            numero = random.randrange(1, 49)
            if not numero in boleto:
                boleto.append(numero)
                break
    reintegro = random.randrange(0, 9)

    return boleto, reintegro

"""Crea la tabla de los numero de la primitiva , la metemos en for para que se repita cada vez que digamos un numero"""

def printear_tabla(boleto):
    for i in range(10):
        for j in range(5):
            if ((10 * j) + i in boleto):
                print("X", end=' ')
            else:
                print((10 * j) + i, end=' ')
        print()
    print("\n")


"""Comprueba los resultados si has acertado o no"""

def comprobar_resultado(boleto, boleto_maquina, reintegro, reintegro_maquina):
    total_aciertos = 0

    print("El boleto de la máquina más el complementario es el siguiente: ")
    for i in range(len(boleto_maquina)):
        print(boleto_maquina[i], end=' ')
    print("\nEl reintegro de la máquina es el siguiente: " + str(reintegro_maquina))

    """Añadimos un contador para que ceunte los aciertos """
    print()
    for j in range(len(boleto)):
        if boleto[j] in boleto_maquina:
            total_aciertos += 1
    """Como en el enunciado nos dice si es menos de 3 no es premiado y mas de 3 si """
    print()
    if(total_aciertos < 3):
        print("Oh, el boleto no ha sido premiado. Solo has acertado " + str(total_aciertos) + " números")
    elif(total_aciertos != 5):
        print("El boleto ha sido premiado. Has acertado " + str(total_aciertos) + " números")
    else:
        print("Te has quedado a un sólo acierto de acertar todos. Has acertado 5")

    if(reintegro == reintegro_maquina):
        print("Has acertado el reintegro")
    else:
        print("No has acertado el reintegro")


def generacion_maquina():
    boleto_maquina, reintegro_maquina = generar_aleatorios(7)
    return boleto_maquina, reintegro_maquina

"""Funcion que nombra a la creacion de numeros aleatorios """

def elegir_aleatoriamente():
    boleto, reintegro = generar_aleatorios(6)
    print("Su elección aleatoria del boleto ha sido la siguiente:")
    printear_tabla(boleto)
    print("Su elección aleatoria del reintegro ha sido la siguiente:")
    print(reintegro)
    return boleto, reintegro


"""Pide al usuario los numeros de boleto manualmente y si no esta en el rango vuelve a preguntar"""

def solicitar_boleto():
    boleto = list()
    print("Rellene los números de su boleto:\n")
    for i in range(6):

        printear_tabla(boleto)
        numero = int(input("Dame un numero de los anteriores\n"))

        while True:
            while (numero < 1 or numero > 49):
                numero = int(input("Número no válido, dame un numero del 1 al 49\n"))

            if numero in boleto:
                numero = int(input("Número no válido, es repetido\n"))
            else:
                boleto.append(numero)
                break

    print("Así ha quedado su boleto:\n")
    printear_tabla(boleto)

    return boleto

"""Pide un número para el reintegro entre un rango de 9 números y si no está vuelve a preguntar"""

def solicitar_reintegro():
    print("Rellene el número del reintegro")
    for i in range(10):
        print(i, end=' ')
    reintegro = int(input("\nDame un numero de los anteriores\n"))

    while (reintegro < 0 or reintegro > 9):
        reintegro = int(input("Número no válido, dame un numero del 0 al 9\n"))

    return reintegro

def elegir_manualmente():
    boleto = solicitar_boleto()
    reintegro = solicitar_reintegro()
    return boleto, reintegro

def main():
    """Creación del menu para ver si quiere hacer la primitiva manualmente o no """

    decision = int(input("Seleccione una de las siguientes opciones:\n" +
              "1. Eliga su boleto y su reintegro\n" +
              "2. Elige aleatoriamente\n"))
    while True:
        if (decision == 1):
            boleto, reintegro = elegir_manualmente()
            break
        elif(decision == 2):
            boleto, reintegro = elegir_aleatoriamente()
            break
        else:
            decision = int(input("Creo que no le he entendido, seleccione 1 o 2\n"))

    boleto_maquina, reintegro_maquina = generacion_maquina()


    """Para continuar el programa y sepamos si hemos acertado , pulsamos un botón"""

    decision = int(input("Pulse el 3 para comprobar sus aciertos: "))
    while True:
        if (decision == 3):
            break
        else:
            decision = int(input("Creo que no le he entendido, seleccione 3: "))

    comprobar_resultado(boleto, boleto_maquina, reintegro, reintegro_maquina)

main()


