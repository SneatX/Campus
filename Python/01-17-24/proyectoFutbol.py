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
            os.system('cls')
            
            eqLo = "" #nombre del equipo local
            punLo = 0   #goles equipo local
            posArrayLo = 0 #Variable para guardar la posicion de la lista en la matriz
            
            eqVi = "" #nombre del equipo visitante
            punVi = 0    #goles equipo visitante
            posArrayVi = 0 #Variable para guardar la posicion de la lista en la matriz
            
            teamEncontrado = False  #Bandera para saber si se encontro el quipo ingresado en la lista de registrados
            while not teamEncontrado:   
                os.system('cls')
                
                eqLo = input("Ingrese el nombre del equipo local: ")
                for i, team in enumerate (equipos): #Recorremos la lista de equipos
                    if(eqLo in team):   
                        teamEncontrado = True   #En caso de encontrar el equipo ingresado cambiamos la variable bandera
                        posArrayLo = i
                        golesCorrectos = True   #Bandera para verificar que los goles ingresados no sean negativos
                        while golesCorrectos: 
                            punLo = int(input("Ingrese los goles anotados por el equipo local: "))
                            if(punLo >= 0):
                                golesCorrectos = False #en caso de ingresar un valor positivo cambiamos la variable bandera
                                equipos[i][5] += punLo
                            else:
                                print("No pueden haber goles negativos...")
                            
                if (not teamEncontrado):
                    print("El equipo ingresado no esta registrado....")
                    os.system('pause')
                
            teamEncontrado = False  #Bandera para saber si se encontro el quipo ingresado en la lista de registrados
            while not teamEncontrado: 
                os.system('cls')
                eqVi = input("Ingrese el nombre del equipo visitante: ")
                for i, team in enumerate(equipos):  #Recorremos la lista de equipos
                    if(eqVi in team):
                        teamEncontrado = True   #En caso de encontrar el equipo ingresado cambiamos la variable bandera
                        posArray = i
                        golesCorrectos = True   #Bandera para verificar que los goles ingresados no sean negativos
                        while golesCorrectos:
                            punVi = int(input("Ingrese los goles anotados por el equipo visitante: "))
                            if(punVi >= 0):
                                golesCorrectos = False #en caso de ingresar un valor positivo cambiamos la variable bandera
                                equipos[i][5] += punVi
                            else:
                                print("No pueden haber goles negativos...")
                        break
                if (not teamEncontrado):
                    print("El equipo ingresado no esta registrado....")
                    os.system('pause')
                    
            #Hallar resultados del partido, ganador, perdedor o empate y guardar los goles en contra######################

            
                       
        else:
            print("No hay equipos registrados hasta el momento...")
            os.system('pause')

    #OPCION NUMERO 3
    elif(op == 3):
        os.system('cls')
        
    else:
        print(equipos)
        os.system('pause')
        
        