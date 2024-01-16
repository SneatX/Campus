sueldo = 14400000

print("Calculo sueldo")
years = int(input("Ingrese la cantidad de años que lleva en la empresa: "))

if(years <= 3):
    aumento = 3
elif(years <= 5):
    aumento = 5
elif (years <= 7):
    aumento = 7
else:
    aumento = 10 #dice el aumento antes y despues de los 10 años, pero no a los 10 años

totalAumento = sueldo*(aumento/100)

print(f"Con {years} años en la empresa tendra un amento del {aumento}% ")
print(f"Sueldo: ${sueldo}")
print(f"totalAumentado: ${totalAumento}")
print(f"Sueldo total: ${(sueldo + (totalAumento))}")