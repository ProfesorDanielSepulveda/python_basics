# Listas, Enumerador, Rango, Max, Comprensión de listas, Random

# Las listas pueden declararse de diversas formas:
# Por ejemplo, podría crear la variable con una lista vacía y luego insertar elementos a través del método append:

# Declaración de una lista vacía y agregando elementos con append

lista = []
lista.append("elemento1")
print(lista) # >['elemento1']

# Otra opción es crear una lista a partir de un rango utilizando un loop
lista = []
for numero in range(1, 5):
    lista.append(numero)
print(lista) # >[1, 2, 3, 4]

# También se pueden declarar listas con objetos predefinidos
lista = ["elemento1", "elemento2", "elemento3"]
print(lista) # >["elemento1", "elemento2", "elemento3"]

# Las listas pueden contener diversos tipos de datos
lista = ["string", 12345, 1.67, ["Es", "una", "lista"], {1, 2, 3}, {1: "Hola", 2: "mundo"}, (1, 2, 3), True]
print(lista) # >["string", 12345, 1.67, ["Es", "una", "lista"], {1, 2, 3}, {1: "Hola", 2: "mundo"}, (1, 2, 3), True]

# Las listas se encuentran indexadas
print(lista[0]) # >"string"
print(lista[2]) # >1.67
print(lista[3][1]) # >"una"
print(lista[6][2]) # >3

# Modificación de elementos en una lista
lista[0] = "Elemento reemplazado"
print(lista) # >["Elemento reemplazado", 12345, 1.67, ["Es", "una", "lista"], {1, 2, 3}, {1: "Hola", 2: "mundo"}, (1, 2, 3), True]

# Enumerate nos permite indexar listas de manera más cómoda
lista = ["Revisemos", "los", "elementos", "de", "una", "lista"]
for indice, item in enumerate(lista):
    print(indice, item)

#> 0 Revisemos
#> 1 los
#> 2 elementos
#> 3 de
#> 4 una
#> 5 lista

# La palabra clave range nos permite generar una numeración entre dos valores
print(56 in range(55, 57)) # >True

# Las palabras claves min y max devuelven los valores mínimos y máximos de un conjunto de datos
lista = [12, 17, 53, 85, 8, 76, 34, 563, 674, 36, 3, 78, 32, 79]
print(max(lista)) # >674
print(min(lista)) # >3

# La comprensión de listas es un atributo que nos permite manejar la construcción de listas de forma más fácil
palabra = "palabra mágica"
nueva_lista = [letra for letra in palabra]
print(nueva_lista) # >['p', 'a', 'l', 'a', 'b', 'r', 'a', ' ', 'm', 'á', 'g', 'i', 'c', 'a']

# Importando métodos desde librerías externas
from random import randint, random, shuffle

#Investiga que hacen estos métodos!

# Ejercicio básico de Loops y listas
# Generar un loop que realice un sorteo entre los números 1 y 9
# Cada vez que uno de los números aparezca, se debe remover ese número del sorteo para que no vuelva a aparecer.
# Que en cada vuelta del sorteo indique los números que quedan disponibles.
# Que el sorteo acabe cuando aparezca un 9
