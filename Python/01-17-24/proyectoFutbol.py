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
    if(op == 1):
        if(len(equipos) > 0):
            os.system('cls')
            noExiste = True
            while noExiste:
                os.system('cls')
                noExiste = False
                nombre = input("Ingrese el nombre del equipo: ")
                for i, item in enumerate (equipos):
                    if(nombre in item):
                        print("Equipo ya agregado anteriormente")
                        noExiste = True
                        os.system('pause')
            equipos.append([nombre, 0, 0, 0, 0, 0, 0 ,0])
        else:
            os.system('cls')
            nombre = input("Ingrese el nombre del equipo: ")
            equipos.append([nombre, 0, 0, 0, 0, 0, 0 ,0])
            
                        
                    
                    
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

        
    elif(op == 3):
        os.system('cls')
        
    else:
        print(equipos)
        os.system('pause')
        