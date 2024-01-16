#se desea realizar un programa que permita leer n numeros enteros positivos, y cuando se ingrese un numero negativo debe mostrar la siguiente informacion:
# total de numeros pares
# total de numeros impares
# promedio de los numeros enteros registrados
# sumatoria total de los numeros enteros registrados
# cuantos numeros son mayores de 50
# cuantos numeros son mayores de 20 y menores de 50
# cuantos numeros son menores de 10

totalPares = 0
sumatoria = 0
may50 = 0
may20men50 = 0
men10 = 0
n = 0

number = int(input("Ingrese el numero, para finalizar ingrese un negativo: "))

while (number >= 0):
    n += 1
    sumatoria += number
    
    if(number%2 == 0):
        totalPares +=1
    if(number > 50):
        may50 +=1
    elif(20 < number < 50):
        may20men50 += 1
    elif(number < 10):
        men10 += 1
    number = int(input("Ingrese el numero, para finalizar ingrese un negativo: "))
    
    
print(f"Total numeros registrados: {n}")
print(f"Total sumatoria numeros: {sumatoria}")
print(f"Promedio numeros registrados: {sumatoria/n}")
print(f"Total numeros pares registrados: {totalPares}")
print(f"Total numeros impares registrados: {n-totalPares}")
print(f"Numeros mayores de 50: {may50}")
print(f"Numeros mayores de 20 menores de 50: {may20men50}")
print(f"Numeros menores que 10: {men10}")
    
