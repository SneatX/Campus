a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

if(a == 0):
    if(b == 0):
        print("No hay solucion unica")
    else:
        print("Sin solucion")
else:
    print(f"Solucion unica: {-b/a}")