palabra = ("holaMundo").upper()
total = len(palabra)

vidas = 3
itsPlaying = True

while itsPlaying:
    letra = (input("Ingrese la letra: ")).upper()
    if (letra in palabra):
        for caracter in palabra:
            if(caracter == letra):
                total -= 1
    else:
        vidas-= 1
    
    if (vidas == 0 or total == 0):
        itsPlaying = False       