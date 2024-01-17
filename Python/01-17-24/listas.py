import os
os.system('cls')
# #Declaracion de listas en py
# numeros = [] #Lista vacia

# print(len(numeros))     #Obtener longitud
# print(type(numeros))    #Ver tipo de variable
# numeros.append(1)       #Agregar elementos a la lista
# print(numeros)
# print(numeros[0])       #Acceder a un elemento en especifico
# numeros[0] = 20         #Modificar elemento de la lista
# print(numeros[0])
# numeros.pop(0)          #Eliminar elemento
# print(len(numeros))

frutas = ["Manzana", "Pera", "Pera"] #Iniciar lista con valores desde el comienzo
frutas.insert(0,"Uvas")     #Insertar un elemento en una posicion especifica

eliminar = input("Ingrese una fruta a eliminar: ")

print(frutas.index("Manzana"))  #Posicion de un elemento

for i in frutas:    #Acceder a los valores
    print(i)

temp = []

for i in frutas:
    if(i == eliminar):
        temp.append(i)
frutas = temp

for i in frutas:
    print(i)
    
    