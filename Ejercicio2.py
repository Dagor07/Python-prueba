"""Solicita dos números al usuario, realiza la suma y muestra el resultado.

Ejemplo:

Ingresa el primer número: 5
Ingresa el segundo número: 3
La suma es: 8.0"""

def numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

while True:
    num1 = input("Ingresa el primer número (puede ser negativo o decimal): ")
    if not numero(num1):
        print("ERROR: Solo se aceptan números (enteros o decimales).")
        continue

    num2 = input("Ingresa el segundo número (puede ser negativo o decimal):")
    if not numero(num2):
        print("ERROR: solo se aceptan números (enteros o decimales)")
    suma = float(num1) + float(num2)
    print("El resultado es", suma)
    break