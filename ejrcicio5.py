def validar_numero(entry):
    try:
        valor = int(entry)
        return True
    except ValueError:
        return False

while True:
    entrada = input("Por favor, ingresa tu edad: ")
    if validar_numero(entrada):
        edad = int(entrada)   
        break 
    else:
        print("Error: ingresa un numero positivo")
        
        

edad_5 = edad + 5
print(f"Su edad dentro de 5 años sera: {edad_5} ")

