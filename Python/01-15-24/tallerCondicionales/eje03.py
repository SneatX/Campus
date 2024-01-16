import math

print("Calculo de figuras geometricas, ¿Que figura quiere calcular?\nT.Triangulo\nC.Circulo")
option = (input("-")).upper()

if(option == "T"):
    base = int(input("Ingrese el tamaño de la base: "))
    altura = int(input("Ingrese el tamaño de la altura: "))
    area = (base * altura)/2
elif(option == "C"):
    radio = int(input("Ingrese el radio del circulo: "))
    area = math.pi * radio * radio
else:
    print("El dato ingresado no es valido")

print(f"El area de la figura es de: {round(area,2)}")
    
    