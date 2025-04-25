def positive_number(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            else:
                print("El valor debe ser mayor a cero.")
        except :
            print("Entrada inválida. Ingresa un número válido.")

def discount():
    while True:
        try:
            discount = float(input("Ingresa el porcentaje de descuento (0-100): "))
            if 0 <= discount <= 100:
                return discount
            else:
                print("El descuento debe estar entre 0 y 100.")
        except :
            print("Entrada inválida. Ingresa un número válido.")

list {
product = input("Nombre del producto: ")
price = positive_number("Precio unitario: ")
amount = positive_number("Cantidad comprada: ")
discount = discount()
}

list.append
subtotal = price * amount
discount = subtotal * (discount / 100)
total = subtotal - discount

print("Resumen de compra")
print("Producto:", product)
print("Subtotal:", subtotal)
print("Descuento:", discount)
print("Total a pagar:", total )