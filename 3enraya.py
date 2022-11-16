"""Importamos las librerias necesarias para hacer el ejercicio"""
from random import randrange
from re import X
import random

"""Ponemos en vector las posiciones del juego y creamos una matriz para nuestro juego"""

posiciones=[0,1,2,3,5,6,7,8,]
matriz=[[1,2,3]
       ,[4,5,6]
       ,[7,8,9]]


"""Inicializamos las variables para que empieze la partida y asignamos los simbolos con los que se juega"""
X = 'X'
O = 'O'
victoria = False
continuar = True

"""Pritea la matriz """
for fila in matriz:
    print("-----------")
    print(str(fila).replace('[', '| ').replace(']', ' |').replace(',',' ').replace('5','X'))
print("-----------")

"""Creamos el algoritmo de nuestro 3 en rayas con matrices """
matriz[1][1] = X
while continuar:


    """Creamos variable para incidicar donde queremos poner nuestra ficha"""

    coordenada= int(input("Dime un número para poner tu ficha: ---> "))
    coordenada -= 1

    """Si la posicion concuerda con la matriz se coloca y se cambia por el simbolo creado anteriormente"""
    if coordenada in posiciones:
        matriz[(coordenada // 3)][(coordenada % 3)]=O
        if matriz[0][0] == matriz[0][1] and matriz[0][1] == matriz[0][2] or \
           matriz[1][0] == matriz[1][1] and matriz[1][1] == matriz[1][2] or \
           matriz[2][0] == matriz[2][1] and matriz[2][1] == matriz[2][2] or \
           matriz[0][0] == matriz[1][0] and matriz[1][0] == matriz[2][0] or \
           matriz[0][1] == matriz[1][1] and matriz[1][1] == matriz[2][1] or \
           matriz[0][2] == matriz[1][2] and matriz[1][2] == matriz[2][2] or \
           matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] or \
           matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0]:
           
           
            for fila in matriz:
                print("-----------")
                print(str(fila).replace('[', '| ').replace(']', ' |').replace(',',' ').replace('5','X').replace('\'', ''))
            print("-----------")
            print("Has ganado la partida")
            break
        posiciones.remove(coordenada)
        programa = random.choice(posiciones)
        matriz[(programa // 3)][(programa % 3)]=X
        if matriz[0][0] == matriz[0][1] and matriz[0][1] == matriz[0][2] or \
           matriz[1][0] == matriz[1][1] and matriz[1][1] == matriz[1][2] or \
           matriz[2][0] == matriz[2][1] and matriz[2][1] == matriz[2][2] or \
           matriz[0][0] == matriz[1][0] and matriz[1][0] == matriz[2][0] or \
           matriz[0][1] == matriz[1][1] and matriz[1][1] == matriz[2][1] or \
           matriz[0][2] == matriz[1][2] and matriz[1][2] == matriz[2][2] or \
           matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] or \
           matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0]:
            
            """Printea de nuevo la matriz para cada tirada"""
            
            for fila in matriz:
                print("-----------")
                print(str(fila).replace('[', '| ').replace(']', ' |').replace(',',' ').replace('5','X').replace('\'', ''))
            print("-----------")
            print("Has perdido la partida ")
            break
        posiciones.remove(programa)
        print("Tu rival ha elegido la casilla: ",programa +1 )
        for fila in matriz:
            print("-----------")
            print(str(fila).replace('[', '| ').replace(']', ' |').replace(',',' ').replace('5','X').replace('\'', ''))
        print("-----------")
        if continuar == False:
            print("La partida se ha acabado")
        if len(posiciones) < 1: 
            continuar = False
            print("Has empatado")
    else:
        print("Pon un número correcto")
        

