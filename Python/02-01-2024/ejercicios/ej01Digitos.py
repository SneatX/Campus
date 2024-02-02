n = int(input("Ingrese el numero entero: "))
contador = 0

if n != 0:
    while n != 0:
        n = n/10
        contador +=1 
        n = int(n)
else:
    contador = 1

    
print(f"Contador; {contador}")
        