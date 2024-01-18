import os
#[nombre, partidos jugados, partidos ganados, partidos perdidos, partidos empate, goles a favor, goles en contra, total puntos]
#[   0  ,         1       ,        2        ,         3        ,        4       ,       5      ,        6       ,      7      ]

equipos = [] 
title = """
    -----------------------------------------
    I    Federacion colombiana de futbol    I
    -----------------------------------------
"""
options = "     -1. Registrar equipo\n     -2. Registro de fechas\n     -3. reportes"
isActive = True

while isActive:
    os.system('cls')
    print(title)
    print(options)
    op = int(input("---"))
    
    #OPCION NUMERO 1
    if(op == 1):
        if(len(equipos) > 0): #Evaluar si la lista tiene mas de 0 nombres
            os.system('cls')
            noExiste = True #inicia en true para entrar al while
            while noExiste: #While en caso de repetir un nombre intentarlo de nuevo
                os.system('cls')
                noExiste = False#se cambia a false para en caso de no encontrar nombres repetidos, finalizar el whilr
                nombre = input("Ingrese el nombre del equipo: ")
                for i, item in enumerate (equipos): #evaluamos si el nombre se encuentra en la lista
                    if(nombre in item):
                        print("Equipo ya agregado anteriormente")
                        noExiste = True #En caso de estar en la lista cambia el valor a True para entrar al while nuevamente
                        os.system('pause')
            equipos.append([nombre, 0, 0, 0, 0, 0, 0 ,0]) #Una vez se salga del while se inserta en la lista
        else: #En caso de no haber nombres en la lista no es necesario validar si el nombre esta repetido
            os.system('cls')
            nombre = input("Ingrese el nombre del equipo: ")
            equipos.append([nombre, 0, 0, 0, 0, 0, 0 ,0])
                    
    #OPCION NUMERO 2                  
    elif(op == 2):
        
        if(len(equipos)>0):
            teamEncontrado = False
            os.system('cls')
            
            eqLo = ""
            eqVi = ""
            
            while not teamEncontrado:
                os.system('cls')
                eqLo = input("Ingrese el nombre del equipo local: ")
                for i, team in enumerate (equipos):
                    if(eqLo in team):
                        punLo = int(input("Ingrese los goles anotados por el equipo local: "))
                        teamEncontrado = True
                if (not teamEncontrado):
                    print("El equipo ingresado no esta registrado....")
                    os.system('pause')
                
            teamEncontrado = False
            
            while not teamEncontrado: 
                os.system('cls')
                eqVi = input("Ingrese el nombre del equipo visitante: ")
                for i, team in enumerate(equipos):
                    if(eqVi in team):
                        punVi = int(input("Ingrese los goles anotados por el equipo visitante: "))
                        teamEncontrado = True
                if (not teamEncontrado):
                    print("El equipo ingresado no esta registrado....")
                    os.system('pause')
                
                    
        else:
            print("No hay equipos registrados hasta el momento...")
            os.system('pause')

    #OPCION NUMERO 3
    elif(op == 3):
        os.system('cls')
        
    else:
        print(equipos)
        os.system('pause')
        