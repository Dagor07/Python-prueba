def validar_numero(entry):
    try:
        valor = float(entry)
        return True
    except ValueError:
        return False

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    entrada = input("Por favor, ingresa la temperatura en grados Celsius: ")
    if validar_numero(entrada):
        celsius = float(entrada)
        break
    else:
        print("Entrada invalida, ingresa un numero valido (positivo, negativo o decimal)")

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit}°F ")





