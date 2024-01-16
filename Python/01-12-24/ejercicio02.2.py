#par o impar con try
n = 0
n = input("Ingrese el numero a evaluar: ")
try:
    if n%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")  
except TypeError:
    print("Valor no valido")