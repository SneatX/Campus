palabra = "holamundo"
vidas = 3
for i in range (len(palabra)):
    print(f"vidas: {vidas}")
    letra = input("letra: ")
    
    if(letra in palabra):
        palabra = palabra.replace(letra, "-")
    else:
        vidas -= 1
    
    if(vidas == 0):
        print("perdiste")
        break