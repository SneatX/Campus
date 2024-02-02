op = int(input("""
               1. Entrada un número entero, y entregue como salida el n-ésimo número de Fibonacci
               2. Entrada un número entero e indique si es o no un número de Fibonacci
               3. Muestre los primeros N numeros de la secuencia
               --> 
               """))
if(op == 1):
    n = int(input("Ingrese la posicion que desea conocer: "))
    lista = [0,1]
    for i in range (n+1):
        lista.append(lista[i] + lista[i+1])
    print(lista[n])
    
elif (op == 2):
    n = int(input("Indique el numero: "))
    i = 0
    lista = [0,1]
    while n > lista[i+1]:
        lista.append(lista[i] + lista[i+1])
        i += 1
    if(n in lista):
        print(f"El numero {n} se encuentra en la secuencia")
    else: 
        print(f"El numero {n} no se encuentra en la secuencia")
        
elif(op == 3):
    n = int(input("Ingrese la cantidad de digitos: "))
    lista = [0,1]
    for i in range (n):
        lista.append(lista[i] + lista[i+1])
    for i,item, in enumerate(lista):
        lista[i] = str(item)
    print(" ".join(lista))