print("Calculo impuestos")
valor = float(input("Ingrese el valor a calcular: "))

if(valor < 0):
    print("Valor ingresado invalido")
else:
    if(valor > 150000):
        total = valor + (valor * 0.19)
        print(f"Impuesto aplicado del 19%, total: ${total}")
    else:
        total = valor + (valor * 0.16)
        print(f"Impuesto aplicado del 16%, total: ${total}")
