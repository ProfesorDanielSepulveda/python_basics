'''Construcción de menús y listas de opciones. Validación Try.
'''

# Los menús y las listas de opciones se construyen de la misma forma y cumplen la misma función:
# Ofrecen una lista de opciones:
# A. Hacer Depósito
# B. Hacer Giro
# C. Consultar Saldo
# D. Salir
# El menú realiza varias acciones para poder auto-validarse.
# En primer lugar, debemos asegurarnos de que el usuario no pueda ingresar una respuesta que pueda producir un error
# o una respuesta que no esté contemplada dentro de las opciones permitidas.
# Luego, por cada respuesta válida, el menú debe generar una opción u ofrecer otro menú.

# Ejemplo utilizando diccionario

opciones = {"A": ". Mensaje", "B": ". Número", "C": ". Salir"}

while True:
    for a, b in opciones.items():
        print(f"{a}{b}")
    respuesta = input("Elige una opción: \n")
    if respuesta.upper() == "A":
        print("Este es un mensaje")
    elif respuesta.upper() == "B":
        print(123)
    elif respuesta.upper() == "C":
        break
    else:
        continue

# La validación con números es ligeramente más compleja, puesto que hay más variables que controlar.
# Esto da pie a que se puedan generar más errores.
# Para manejar errores se usa TRY

opciones = {1: "palabra", 2: "numero", 3: "salir"}
while True:
    for a, b in opciones.items():
        print(f"{a}. {b}")
    respuesta = input("Ingrese una opción: \n")
    try:
        if int(respuesta) == 1:
            print("Este es un mensaje")
        elif int(respuesta) == 2:
            print(123)
        elif int(respuesta) == 3:
            break
    except:
        continue

# Try sirve para manejar errores y lo hace a través de cuatro palabras claves:
# TRY prueba en busca de un error, si no hay errores, ejecuta el contenido
# EXCEPT comando si es que hay errores
# ELSE comando si es que no hay errores
# FINALLY comando a ejecutar independiente del resultado del try


# Ejercicio:
# 01

'''Vamos a construir un juego llamado "Adivina el Número".
En este juego, el programa seleccionará aleatoriamente un número entre 1 y 100
Se deberá adivinar cuál es ese número en tan solo 8 intentos

Se debe dar la bienvenida al juego y explicar las reglas básicas.
Luego, se tendrá la oportunidad de ingresar tus intentos para adivinar el número.
Si se ingresa un número fuera del rango o no válido, se debe perder un intento.
Después de cada intento, el programa debe dar pistas sobre si el número elegido
es mayor o menor que el número secreto.

Al adivinar el número en menos de 8 intentos, se ganará el juego y el programa
indicará cuantos intentos se utilizaron
Pero si se agotan los 8 intentos sin adivinar el número,
Se perderá el juego y el programa debe indicar cual era el número secreto.
'''

# EJEMPLOS DE OUTPUT
# AL perder:
'''
=======================
===ADIVINA EL NUMERO===
=======================

He elegido un número al azar entre el 1 el 100
Tienes 8 intentos para adivinarlo.

Por favor, elige un número entre el 1 y el 100:
80

==================================================

Has elegido un número MENOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
70

==================================================

Has elegido un número MENOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
50

==================================================

Has elegido un número MENOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
40

==================================================

Has elegido un número MENOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
30

==================================================

Has elegido un número MENOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
20

==================================================

Has elegido un número MENOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
10

==================================================

Has elegido un número MENOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
10

==================================================

Has elegido un número MENOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Has agotado tus intentos. El número secreto era 92. ¡Adiós!
'''


# Al ganar:
'''
=======================
===ADIVINA EL NUMERO===
=======================

He elegido un número al azar entre el 1 el 100
Tienes 8 intentos para adivinarlo.

Por favor, elige un número entre el 1 y el 100:
50

==================================================

Has elegido un número MAYOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
40

==================================================

Has elegido un número MAYOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
30

==================================================

Has elegido un número MENOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
35

==================================================

Has elegido un número MAYOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
33

==================================================

Has elegido un número MAYOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
32

==================================================

Has elegido un número MAYOR que el número secreto. ¡Inténtalo de nuevo!

==================================================

Por favor, elige un número entre el 1 y el 100:
31

==================================================

¡Has adivinado el número secreto y has ganado! ¡Felicidades!
Utilizaste 7 intentos.

==================================================
'''

