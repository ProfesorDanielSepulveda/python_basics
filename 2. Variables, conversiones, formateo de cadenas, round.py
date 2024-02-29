"""
Variables. Int y Float. Conversiones. Formatear cadenas. Operadores. Round
"""

#Una variable es un trozo de código capaz de almacenar un dato.
#Una variable puede almacenar un dato de cualquier tipo
#Aquí un ejemplo de una variable:

variable = "esto es una variable y guarda texto"

#por convención, los nombres de las variables se escriben siempre en minúsculas
#si es necesario, se pueden agregar _ para aumentar la legibilidad.
#ejemplos de nombres de variable:

#numeros = xxxxxxx
#numeros_filtrados = xxxxxxx
#nombre_usuario = xxxxxxx
#apellido_usuario = xxxxxxx
#direccion = xxxxxxx

#Además, las variables no pueden tener nombres de comandos:
#por ejemplo, no podemos tener una variable que se llame print o input.

#Revisa el resto de las convenciones pep8:
'''
https://peps.python.org/pep-0008/
'''
'''

╔═══════════════════════════════════════════════════════════════════════════╗
║ Recomendación PEP8                                                        ║
║                                                                           ║
║───────────────────────────────────────────────────────────────────────────║
║ Descripción                                                               ║
║───────────────────────────────────────────────────────────────────────────║
║ Utiliza sangrías de 4 espacios                                            ║
║                                                                           ║
║───────────────────────────────────────────────────────────────────────────║
║ Limita la longitud de las líneas a 79 caracteres                          ║
║                                                                           ║
║───────────────────────────────────────────────────────────────────────────║
║ Utiliza líneas en blanco de manera adecuada                               ║
║                                                                           ║
║───────────────────────────────────────────────────────────────────────────║
║ Importa módulos en líneas separadas al inicio del script                  ║
║                                                                           ║
║───────────────────────────────────────────────────────────────────────────║
║ Usa espacios alrededor de operadores                                      ║
║                                                                           ║
║───────────────────────────────────────────────────────────────────────────║
║ Evita líneas de código con más de un comando                              ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

'''


#una variable puede ser LLAMADA
#al llamar una variable, la estamos incorporando a una función o comando
#llamar es la forma de darle uso a una variable
#Aquí se llama a la variable anterior con el comando print:

print(variable) #> esto es una variable y guarda texto

#A cada variable le corresponde un tipo de dato:
#Revisemos de que tipo es esta variable:

print(type(variable)) #> <class 'str'>

#Este tipo de dato es STR o string, lo que significa que es texto.
#Casi cualquier cosa entre comillas es texto.
#El contenido de una variable puede alterarse siempre que queramos
#Incluso si eso significa reemplazar el contenido con un tipo de dato distinto

print(variable) #> esto es una variable y guarda texto

print(type(variable)) #> <class 'str'>

#Ahora vamos a sobreescribir la variable:

variable = 123456

#¿Qué tiene la variable dentro ahora y de qué tipo es?

print(variable) #> 123456

print(type(variable)) #> <class 'int'>

#Este tipo de dato es INT o integer, lo que significa que son números ENTEROS.
#Cualquier número no flotante es un entero.

#Una variable puede almacenar CASI cualquier cosa, incluso comandos o funciones
#El tipo de dato que almacena una variable dependerá de lo que tenga almacenado y cambiará para ajustarse.
#Si bien las variables son ajustables,
#A veces no pueden interactuar entre ellas si pertenecen a tipos totalmente distintos:

palabras = "hola mundo!"
numeros = 123456
print(palabras + numeros)

'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

#ENTEROS:
#Algunos tipos de dato además del STR son el INT y el FLOAT
#Aquí hay algunos ejemplos de INT:

entero1 = 57603
entero2 = -12367
entero3 = 0 + 15

# verificacion
#Vamos a verificar los tipos de datos:
print(type(entero1)) #> <class 'int'>
print(type(entero2)) #> <class 'int'>
print(type(entero3)) #> <class 'int'>


# floats
#Aquí hay algunos ejemplos de FLOAT
flotante1 = 3.14
flotante2 = 0.15 + 3.14
flotante3 = 0.5 + 0.5

# verificacion
#Vamos a verificar los tipos de datos:
print(type(flotante1)) #> <class 'float'>
print(type(flotante2)) #> <class 'float'>
print(type(flotante3)) #> <class 'float'>

# conversiones
#Puedo realizar conversiones a las variables. En este caso vamos a convertir la variable flotante 5.6 en entero:

flotante = 5.6
print(int(flotante)) #> 5

#Al imprimir el flotante como int, simplemente se eliminará toda la sección de decimales
#ES MUY IMPORTANTE distinguir las acciones que trabajan 'en el lugar'
#de las que generan un cambio y 'devuelven' un valor o una acción
#En este caso, la acción int(flotante) se está lanzando a la pantalla a través de print
#Pero no se está almacenando en ningún lugar.
#Eso quiere decir que ACTUA SOLO en ese lugar y no genera o devuelve ningún nuevo valor
#Vamos a generar un cambio real en la variable. Revisemos el valor de la variable y su tipo:

print(flotante) #> 5.6

print(type(flotante)) #> <class 'float'>

#Ahora vamos a generar la conversión y a almacenar esa conversión dentro de la misma variable:

flotante = int(flotante)

#Volvamos a verificar el contenido y el tipo:

print(flotante) #> 5

print(type(flotante)) #> <class 'int'>

# Formatear cadenas
#El proceso de concatenación nos permite juntar variables en cadenas:
#por ejemplo

valor1 = "Daniel"
valor2 = "Sepúlveda"
valor3 = 18

print("El profesor de la asignatura es " + valor1 + " " + valor2) #> El profesor de la asignatura es Daniel Sepúlveda

#Sin embargo, este proceso puede presentar fallos si intentamos concatenar tipos de datos distintos.
#Sin mencionar que es muy difícil realizar el llamado de los valores uno por uno con comillas, respetando espacios y signos +
#Para estos efectos es mucho más fácil formatear la cadena para poder representar los valores

#para poder formatear una cadena debemos agregar la letra 'f' delante y representar las variables entre {}

print(f"El profesor de la clase es {valor1} {valor2} y tiene {valor3} años.") #> El profesor de la clase es Daniel Sepúlveda y tiene 18 años.

# operadores
#Los operadores aritméticos en python son los siguientes:
# + sumar
# - restar
# * multiplicar
# / dividir
# // división al piso
# ** potenciado a
# % modulo de
print(f"{5} + {5} es igual a {10}") #> 5 + 5 es igual a 10

print(f"{5} - {5} es igual a {0}") #> 5 - 5 es igual a 0

print(f"{5} * {5} es igual a {25}") #> 5 * 5 es igual a 25

print(f"{25} / {5} es igual a {5}") #> 25 / 5 es igual a 5

print(f"{22} // {7} es igual a {3}") #> 22 // 7 es igual a 3

print(f"{5} ** {2} es igual a {25}") #> 5 ** 2 es igual a 25

print(f"El módulo de {22} // {7} es igual a {1}") #> El módulo de 22 // 7 es igual a 1

#Los operadores de comparación en python son los siguientes:
# > Mayor que
# >= Mayor o igual que
# < Menor que
# <= Menor o igual que
# == Igual que
# != Diferente
# in -> Está en
# not in -> No está en

#Los operadores establecen comparaciones entre dos elementos y devuelven un resultado de tipo bool
#Un valor booleano solo puede tener dos valores: verdadero o falso

print(4 > 8) #> False

print(78 >= 78) #> True

print("rosa" == "rosa") #> True

print("rosa" != 89) #> True

print("rosa" in "La rosa es bella") #> True

print("rosa" not in "La rosa es bella") #> False

# ROUND
#La palabra clave round() redondea un número o valor establecido a su valor
#mas cercano:

print(round(5.4)) #> 5

print(round(5.6)) #> 6


# 01
# desarrolla un algoritmo que pregunte al usuario su nombre y sus apellidos
# que le pida un número flotante.
# que le pida un número entero.
# que muestre en una cadena su nombre y los números que escogio.
# que muestre en una cadena el tipo de datos de los numeros que escogio.
# que convierta el flotante en entero, devuelva su valor y su tipo de dato.

# 02
# Desarrolla un algoritmo que pida a un usuario los siguientes datos:
# Nombre, apellido, direccion, telefono, tipo domicilio (casa o dpto)
# Luego, debe emitir el siguiente output:
# (Asegúrate de respetar los espaciados y tabulados)

'''
=========BOLETA=========
Nombre:   NOMBRE
Apellido: APELLIDO
Celular:  123456789

========================
======DESPACHAR A:======
========================

Direcc:   DIRECCION
tipo:     TIPO
'''
