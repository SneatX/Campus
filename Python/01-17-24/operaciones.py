import os
os.system('cls')
title = """
    +++++++++++++++++++++++++++++
    +   Operaciones con listas  +
    +++++++++++++++++++++++++++++
"""
options = "1. Agregar camper\n2. Eliminar Camper\n3. Buscar Camper\n4. Salir"
isActive = True
campers = []
while isActive:
    os.system('cls')
    print(title)
    print(options)
    op = int(input(" -- "))
    if(op == 1):
        id = str(len(campers)).zfill(5)
        nombre = input("Ingrese el nombre del camper a agregar: ")
        campers.append([id, nombre]) #Agregamos una lista a Campers con la informacion del estudiante
    elif(op == 2):
        nombre = input("Ingrese el nombre del camper a eliminar: ")
        
        for i,item in enumerate (campers): #Buscamos que el nombre se encuentre en alguna lista de campers
            if(nombre in i): #Si el nombre esta en campers, elimina la posicion de la lista en campers
                campers.pop(i)
                break
    elif(op == 3):
        nombre = input("Ingrese el nombre del camper a buscar: ")
        for i, item in enumerate (campers): #Recorremos la lista campers en busca del nombre
            if (nombre in item): #Si lo encontremos tomamos su informacion
                print(f"Posicion:{i}")
                print(f"Codigo:{item[0]}")
                print(f"Nombre:{item[1]}")
        os.system('pause')
    elif(op == 4):
        isActive = False
        print("Fin del programa\nGracias por utilizarlo...")
        os.system('pause')
    else:
        os.system('cls')
        print("Opcion elegida invalida")
        os.system('pause')