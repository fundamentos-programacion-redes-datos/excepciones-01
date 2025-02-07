"""
    Manejo de excepciones en Python
"""

# Se inicia un bloque try para capturar posibles errores
try:
    # Se solicita al usuario un valor para el numerador
    numerador = input("Ingrese un valor numérico como numerador: ")
    # Se convierte la entrada del usuario a tipo float
    numerador = float(numerador)
    
    # Se solicita al usuario un valor para el denominador
    denominador = input("Ingrese un valor numérico como denominador: ")
    # Se convierte la entrada del usuario a tipo float
    denominador = float(denominador)
    
    # Se realiza la operación de división
    division = numerador / denominador
    
    # Se imprime el resultado de la división, formateado con 2 decimales
    print(f"La división entre {numerador}/{denominador} es igual a {division:.2f}")

# Captura la excepción ValueError, que ocurre si la conversión a float falla
except ValueError:
    # Se muestra un mensaje de error si el usuario ingresa un valor no numérico
    print("Error: Se debe ingresar un valor numérico válido.")

# Mensaje final del programa, se ejecuta independientemente de si hubo error o no
# al ingresar un valor no numérico para numerador o denominador
print("Fin del programa")
