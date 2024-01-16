print("Calculo area de un rectangulo")

base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("ingrese la altura del rectangulo: "))

if(base > 0 and altura > 0):
    print(f"El area del rectangulo es de: {(base * altura)}")
else:
    print("Los datos ingresados no son validos")
