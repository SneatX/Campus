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
        os.system('cls')
        nombre = input("Ingrese el nombre del equipo: ")
        equipos.append([nombre,0,0,0,0,0,0,0])
        print(equipos[0])
        os.system('pause')
        
    elif(op == 2):
        os.system('cls')
        eqLo = input("Ingrese el nombre del equipo local: ")
        punLo = int(input("Ingrese los goles anotados por el equipo locar: "))
        
        for i,equipo in enumerate(equipos):
            pass
        
        eqVi = input("Ingrese el nombre del equipo visitante: ")
        punVi = int(input("Ingrese los goles anotados por el equipo visitante: "))
        
        
        
    elif(op == 3):
        os.system('cls')
        
    else:
        os.system('cls')
