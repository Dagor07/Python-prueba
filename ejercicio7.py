def validar_numero(entry):
    try:
        valor = int(entry)
        return True
    except ValueError:
        return False

while True:
    entrada = input("Por favor, ingresa un numero entero ")
    if validar_numero(entrada):
        edad = int(entrada)
        break
    else:
        print("Error: ingresa un numero entero")




numero = int(input("Por favor, ingresa un número: "))


if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")