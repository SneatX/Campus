contador = 0

while (contador < 4):
    for i in range (150, 410, 1):
        numero = str(i)
        suma = int(numero[0])**3 + int(numero[1])**3 + int(numero[2])**3
        
        if(suma == i):
            print(f"{numero[0]}^3 + {numero[1]}^3 + {numero[2]}^3 == {suma}")
            contador +=1
        
        