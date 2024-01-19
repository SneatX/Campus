import os
from tabulate import tabulate
#[nombre, partidos jugados, partidos ganados, partidos perdidos, partidos empate, goles a favor, goles en contra, total puntos]
#[   0  ,         1       ,        2        ,         3        ,        4       ,       5      ,        6       ,      7      ]

equipos = [] 
title = """
    -----------------------------------------
    I    Federacion colombiana de futbol    I
    -----------------------------------------
"""
options = "     -1. Registrar equipo\n     -2. Registro de fechas\n     -3. reportes\n     -4.Salir"
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
        if(len(equipos)> 1):
            os.system('cls')
            eqLo = "" #nombre del equipo local
            golesLo = 0   #goles equipo local
            posArrayLo = 0 #Variable para guardar la posicion de la lista en la matriz
            eqVi = "" #nombre del equipo visitante
            golesVi = 0    #goles equipo visitante
            posArrayVi = 0 #Variable para guardar la posicion de la lista en la matriz
            teamEncontrado = False  #Bandera para saber si se encontro el quipo ingresado en la lista de registrados
            print("Equipos disponibles: ")
            for i in range (len(equipos)):
                print(equipos[i][0])
            while not teamEncontrado:         
                eqLo = input("Ingrese el nombre del equipo local: ")
                for i, team in enumerate (equipos): #Recorremos la lista de equipos
                    if(eqLo in team):   
                        teamEncontrado = True   #En caso de encontrar el equipo ingresado cambiamos la variable bandera
                        posArrayLo = i
                        golesCorrectos = True   #Bandera para verificar que los goles ingresados no sean negativos
                        while golesCorrectos: 
                            golesLo = int(input("Ingrese los goles anotados por el equipo local: "))
                            if(golesLo >= 0):
                                golesCorrectos = False #en caso de ingresar un valor positivo cambiamos la variable bandera
                                equipos[i][5] += golesLo
                            else:
                                print("No pueden haber goles negativos...")
                if (not teamEncontrado):
                    print("El equipo ingresado no esta registrado....")
                    os.system('pause')
            teamEncontrado = False  #Bandera para saber si se encontro el quipo ingresado en la lista de registrados
            os.system('cls')
            print("Equipos disponibles: ")
            for i in range (len(equipos)):
                if(equipos[i][0] != eqLo):
                    print(equipos[i][0]) 
            while not teamEncontrado: 
                eqVi = input("Ingrese el nombre del equipo visitante: ")
                for i, team in enumerate(equipos):  #Recorremos la lista de equipos
                    if(eqVi in team):
                        if(eqVi != eqLo):
                            teamEncontrado = True   #En caso de encontrar el equipo ingresado cambiamos la variable bandera
                            posArrayVi = i
                            golesCorrectos = True   #Bandera para verificar que los goles ingresados no sean negativos
                            while golesCorrectos:
                                golesVi = int(input("Ingrese los goles anotados por el equipo visitante: "))
                                if(golesVi >= 0):
                                    golesCorrectos = False #en caso de ingresar un valor positivo cambiamos la variable bandera
                                    equipos[i][5] += golesVi
                                else:
                                    print("No pueden haber goles negativos...")
                            break
                        else:
                            print("El equipo visitante y local son el mismo...")
                            os.system('pause')
                if (not teamEncontrado):
                    print("El equipo ingresado no esta registrado....")
                    os.system('pause')
            #Sumar a partidos jugados
            equipos[posArrayLo][1] += 1
            equipos[posArrayVi][1] += 1
            #Hallar resultados del partido, ganador, perdedor o empate y guardar los goles en contra
            if(golesLo > golesVi):
                equipos[posArrayLo][2] += 1 #Partidos ganados Locales
                equipos[posArrayVi][3] += 1 #Partidos perdidos Visitas
                equipos[posArrayLo][6] += golesVi #Goles en contra Locales
                equipos[posArrayVi][6] += golesLo #Goles en contra Visitas
                equipos[posArrayLo][7] += 3 #Suma de 3 puntos por ganar el partido
            elif(golesVi > golesLo):
                equipos[posArrayVi][2] += 1 #Partidos ganados Visitas
                equipos[posArrayLo][3] += 1 #Partidos perdidos Locales
                equipos[posArrayLo][6] += golesVi #Goles en contra Locales
                equipos[posArrayVi][6] += golesLo #Goles en contra Visitas
                equipos[posArrayVi][7] += 3 #Suma de 3 puntos por ganar el partido
            else:
                equipos[posArrayLo][4] += 1 #Partido empatado Locales
                equipos[posArrayVi][4] += 1 #Partido empatado Visitas
                equipos[posArrayLo][6] += golesVi #Goles en contra locales
                equipos[posArrayVi][6] += golesLo #Goles en contra Visitas
                equipos[posArrayLo][7] += 1 #Suma de 1 punto por empate
                equipos[posArrayVi][7] += 1 #Suma de 1 punto por empate  
        else:
            print("No hay suficientes equipos registrados...")
            os.system('pause')
    #OPCION NUMERO 3
    elif(op == 3):
        os.system('cls')
        opcionesReportes = """
    1. Nombre del equipo que mas goles anoto
    2. Nombre del equipo que mas puntos tiene
    3. Nombre del equipo que mas partidos gano
    4. Total de goles anotados por todos los equipos
    5. Promedio de goles anotados en el torneo
    6. Salir
        """
        print(opcionesReportes)
        opReporte = int(input("Que reporte desea revisar?: "))
        if( 1 <= opReporte <= 3):
            os.system('cls')
            if (opReporte == 1):
                indice = 5 #indice donde se almacenan los goles de los equipos
                print("-----Tabla ordenada por cantidad de goles de manera descendente-----")
            elif (opReporte == 2):
                indice = 7 #indice donde se almacenan puntos de cada equipo
                print("-----Tabla ordenada por cantidad de puntos de manera descendente-----")
            else:
                indice = 2 #indice donde se almacenan los partidos ganados
                print("-----Tabla ordenada por cantidad de partidos ganados de manera descendente-----")
            listaOrdenada = equipos
            for i in range (len(listaOrdenada)):
                for j in range(i+1):
                    if(listaOrdenada[i][indice] > listaOrdenada[j][indice]):
                        aux = listaOrdenada[j]
                        listaOrdenada[j] = listaOrdenada[i]
                        listaOrdenada[i] = aux
            print(tabulate(listaOrdenada, headers=["Nombre" , "Partidos jugados" , "Partidos ganados", "Partidos perdidos", "Partidos empatados", "goles a favor", "goles en contra", "total puntos"]))
            os.system('pause')
        elif (opReporte == 4):
            os.system('cls')
            totalGoles = 0
            for i in equipos:
                totalGoles += i[5]
            print(f"Total goles realizados en el torneo: {totalGoles}")
            os.system('pause')
        elif (opReporte == 5):
            os.system('cls')
            partidosRealizados = 0
            for i in equipos:
                partidosRealizados += i[1]
            print(f"Partidos realizados: {partidosRealizados}")
            os.system('pause')
        else:
            print("Opcion ingresada incorrecta")
            
    elif(op==4):
        os.system('cls')
        print("Al salir del programa todos los datos anteriormente ingresados seran borrados")
        print("Para salir ingrese la tecla S")
        print("Para cancelar ingrese cualquier otra tecla")
        salir = input("¿Desea continuar?: ")
        if(salir.upper() == "S"):
            isActive = False
            os.system('cls')
            print("Gracias por utilizar el programa :3")
            os.system('pause')
        
        
        
        