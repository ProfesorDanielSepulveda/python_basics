'''Operadores lógicos y Control de Flujo
'''

# Operadores lógicos
# Los operadores lógicos nos permiten verificar más de una condición al mismo tiempo.
# Los operadores lógicos son:
# and -> 'Y'
# or -> 'O'
# not -> 'NO'

# Ejemplos de uso de operadores lógicos
print(4 < 5 and 7 < 10)
print("hola" == "hola" and 10 == 14)
print("Daniel" == "Buen Profe" and 17 != 17)

print("deuda" in "el cliente tiene una deuda" or 10 != 17)
print(0 > -1 or "rosa" == "rosa")
print("ya" in "no se me ocurre nada" or 100 > 200)

print(not 100 > 200)
print(not "sangre" in "Si había sangre, el acusado es culpable")
print(not 100 == 100)

# Control de Flujo
# El control de flujo es esencial en la programación en Python.

# Ejemplos de uso de estructuras de control if-else
#01
if 50 > 25:
    print("50 es mayor que 25")

#02
valor = 100

if valor > 100:
    print(f"{valor} es mayor que 100")
elif valor >= 100:
    print(f"{valor} es mayor o igual que 100")
else:
    print(f"{valor} No es mayor que 100")

# Control de flujo anidado
from random import randint

dice = randint(1, 6)
print("Has lanzado un dado")
if dice <= 3:
    print(f"Tu resultado es {dice}, que es menor o igual a 3. No es un buen resultado")
    if dice == 1:
        print("Tu resultado es considerablemente malo. Lo lamento.")
    else:
        print("Tu resultado podría haber sido peor. ¡Ánimo!")
elif dice > 3 and dice < 6:
    print(f"Tu resultado es {dice}, que es mayor a 3, pero no es 6")
    if dice == 5:
        print("Tu resultado fue casi un 6. ¡Tan cerca!")
else:
    print(f"Tu resultado es {dice}. ¡Es increíble!")




# Ejercicio 1: Constructor de Oraciones
# Genera un programa que ofrezca al usuario la oportunidad de elegir entre los siguientes tres grupos de palabras
# Jacinto - Maria - Esa persona
# es - no es - creo que es
# amable - gentil
# y que luego construya una oración con ellas.
# Las palabras deben reunirse a través de selecciones numéricas (1,2,3).



# Construye un pequeño juego de rol en el que ofrezcas texto al usuario
# El usuario debe poder tomar decisiones usando teclas numericas
# Cada decisión debe llevar a una rama de la historia distinta.
# Intenta anidar al menos tres controles de flujo
