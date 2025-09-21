print("venta de productos")
total_de_ventas = float(input("ingrese el total de la venta: "))
descuento = float(input("ingrese el descuento: "))

def calcular_descuento(total_de_ventas, descuento = descuento):
 total = (total_de_ventas * descuento) / 100
 return total
if descuento == "" :
    resultado = calcular_descuento(total_de_ventas)
else:
    resultado = calcular_descuento(total_de_ventas, descuento)


print(total_de_ventas - resultado)

