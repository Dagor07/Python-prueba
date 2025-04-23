"""4. Área de un rectángulo

Pide al usuario la base y la altura de un rectángulo y calcula su área.

Ejemplo:

Ingresa la base del rectángulo: 4
Ingresa la altura del rectángulo: 5
El área del rectángulo es: 20.0"""

def numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

while True:
    base = input("Ingresa el primer número (puede ser decimal): ")
    if not numero(base):
        print("ERROR: Solo se aceptan números (enteros o decimales).")
    if float(base) <0:
        print("ERROR: Solo se aceptan números positivos")
        continue

    altura = input("Ingresa el segundo número (puede ser decimal):")
    if not numero(altura):
        print("ERROR: Solo se aceptan números (enteros o decimales)")
    if float(altura) <0:
        print("ERROR: Solo se aceptan números positivos")
        continue
        area = float(base) * float(altura)
    print("El área es", area)
    break