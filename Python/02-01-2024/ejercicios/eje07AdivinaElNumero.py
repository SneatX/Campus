from random import randrange

print("\nJuego 1\n")
firstGame = True
tries = 0
n = randrange(101)

while firstGame:
    tries += 1
    number = int(input(f"intento: {tries}: "))
    
    if(n > number):
        print(f"El numero es mayor que {number}")
    elif( n < number):
        print(f"El numero es menor que {number}")
    else:
        firstGame = False
print(f"Correcto, adivinaste en: {tries} intentos\n")

print("\nJuego 2\n")
secondGame = True
tries = 0
menor = 0
mayor = 100

while secondGame:
    tries+=1
    number = int((mayor + menor)/2)
    print(f"Intento: {tries}: {number}")
    op = input("-_) ")
    
    if(op == ">"):
        menor = number
    elif(op == "<"):
        mayor = number
    else:
        secondGame = False
print(f"Adivine en: {tries} intentos :3")

    
        
        
