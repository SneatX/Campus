horas = float(input("Ingrese el total de horas trabajadas: "))
print("Seleccione:\n-1:Planta\n-2:Administrativo")
selec = int(input("--"))
if(selec == 1):
    print(f"Total a pagar: ${(horas * 20000)}")
elif(selec == 2):
    print(f"Total a pagar: ${(horas * 10000)}")
else:
    print("Seleccion erronea")


