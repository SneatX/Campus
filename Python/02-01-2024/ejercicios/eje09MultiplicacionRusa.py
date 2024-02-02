multiplicador = int(input("Ingrese el multiplicador: "))
multiplicando = int(input("Ingrese el multiplicando: "))

suma = 0

while (multiplicador >= 1 ):
    if(multiplicador%2 != 0):
        suma += multiplicando
    multiplicador = int(multiplicador/2)
    multiplicando = multiplicando * 2

print(f"Resultado: {suma}")