print("Consumo restaurante")

consumo = int(input("Ingrese lo consumido en pesos colombianos: "))
if (consumo > 130000):
    total = consumo-(consumo * 0.15)
    print("Aplica descuento")
else:
    total = consumo
    print("No aplica descuento")


print(f"Total a pagar: {round(total,2)}")