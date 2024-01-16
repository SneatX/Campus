n1 = int(input("Ingrese el numero 1: "))
n2 = int(input("Ingrese el numero 2: "))
n3 = int(input("Ingrese el numero 3: "))

if(n1 > n2 and n1 > n3):
    pos1 = n1
    if(n2 > n3):
        pos2 = n2
        pos3 = n3
    else:
        pos2 = n3
        pos3 = n2
        
if(n2 > n1 and n2 > n3):
    pos1 = n2
    if(n1 > n3):
        pos2 = n1
        pos3 = n3
    else:
        pos2 = n3
        pos3 = n1
        
if(n3 > n1 and n3 > n2):
    pos1 = n3
    if(n1 > n2):
        pos2 = n1
        pos3 = n2
    else:
        pos2 = n2
        pos3 = n1
        
print(f"\nMayor: {pos1}")
print(f"Intermedio: {pos2}")
print(f"Menor: {pos3}")