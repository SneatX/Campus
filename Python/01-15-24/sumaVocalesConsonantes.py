import os
os.system('cls')

mensaje = input("Ingrese el mensaje a evaluar: ")
consonantes = int(0)
vocales = int(0)
lstVocales = "AEIOU"

for caracter in mensaje:
    if caracter.upper() in lstVocales:
        vocales = vocales + 1
    elif caracter.isalpha():
        consonantes = consonantes + 1

print(f"El total de vocales es de: {vocales}")
print(f"El total de consonantes es de: {consonantes}")


for i, item in enumerate(mensaje): #Enumerate convierte el msj en un array
    print(f"Pos: {i}, Caracter: {item}")
    mensaje = mensaje.replace(item, "-")
    print(mensaje)