n = int(input("Ingrese la cantidad de datos que va a ingresar: "))
divisor = 0
for i in range(n):
    number = int(input(f"Ingrese el numero {i+1}: "))
    divisor += (1/number)
media = n / divisor

print(f"Media armonica: {media}")
