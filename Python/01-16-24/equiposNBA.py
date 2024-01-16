try:
    nombre1= input("Ingrese el nombre del equipo 1: ")
    canastas1= int(input("Ingrese el numero de canastas del equipo 1: "))
    nombre2= input("Ingrese el nombre del equipo 2: ")
    canastas2= int(input("Ingrese el numero de canastas del equipo 2: "))
except ValueError:
    print("Dato ingresado no valido")
    
else:
    nombreGanador= ""
    nombrePerdedor =""
    punGanador = 0
    punPerdedor = 0

    print("\n-----RESUMEN PARTIDO-----")

    if(canastas1 > canastas2):
        print(f"Equipo ganador: {nombre1} con {canastas1} canastas")
        print(f"Equipo perdedor: {nombre2} con {canastas2} canastas")
    elif(canastas1 < canastas2):    
        print(f"Equipo ganador: {nombre2} con {canastas2} canastas")
        print(f"Equipo perdedor: {nombre1} con {canastas1} canastas")
    else:
        print(f"No hay equipo ganador, empate")
        print(f"Equipo 1: {nombre1}")
        print(f"Equipo 2: {nombre2}")
        
    print(f"Con una diferencia de {abs(canastas1-canastas2)} canastas")
    
    

