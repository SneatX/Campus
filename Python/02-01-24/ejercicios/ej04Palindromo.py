number = input("Ingrese el numero: ")
tamaño = len(number)
newNumber = list(range(tamaño))

for i in range(len(number)):
    newNumber[tamaño-i-1] = number[i]
    
newNumber = "".join(newNumber)

if (number == newNumber):
    print(f"{number} es un numero palindromo")
else:
    print(f"{number} no es un numero palindromo")