"""
    Manejo de excepciones en Python
"""

numerador = input("Ingrese un valor numérico como numerador: ")
numerador = float(numerador)


denominador = input("Ingrese un valor numérico como denominador:  ")
denominador = float(denominador)

division = numerador / denominador

print(f"La división entre {numerador}/{denominador} es igual a {division:.2f}")
print("Fin del programa")

"""
Ejecución 1

Ingrese un valor numérico como numerador: 10
Ingrese un valor numérico como denominador:  3

Salida 1

La división entre 10.0/3.0 es igual a 3.33

----------------------------------
Ejecución 2

Ingrese un valor numérico como numerador: 10
Ingrese un valor numérico como denominador:  a

Salida:

Traceback (most recent call last):
denominador = float(denominador)
ValueError: could not convert string to float: 'a'

"""
