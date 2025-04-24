def validar(entry):
    try:
        valor = float(entry)
        return True
    except ValueError:
        return False

def celsiustofahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    entrada = input("Por favor, ingresa la temperatura en grados Celsius: ")
    if validar(entrada):
        celsius = float(entrada)
        break
    else:
        print("Entrada invalida, ingresa un numero valido (positivo, negativo o decimal)")

fahrenheit = celsiustofahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit}°F ")
