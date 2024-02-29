"""
Métodos string. Propiedades string. Listas. Diccionarios. Tuples. Sets. Bool.
"""

# Métodos string
# Un método aplica una acción a un elemento contenido en una variable o a un dato según su tipo.
# Todos los tipos de datos tienen sus propios métodos.
# Los principales métodos de los string (aunque hay muchos más) son los siguientes:

# upper -> MAYÚSCULAS
# lower -> minúsculas
# split -> convierte la cadena en una lista
# join -> une una lista en una cadena
# find -> encuentra un substring
# replace -> reemplaza elementos

# La gran mayoría de los métodos operan de la siguiente manera:
# Dada una variable que almacena un x tipo de dato, a esa variable se pueden aplicar los métodos de ese tipo de dato.
# Por ejemplo, si la una variable contiene str, entonces se le podrán aplicar los métodos de string.
# La gran mayoría de los métodos se aplican con la forma:
# variable.metodo(data)
# donde variable es la variable, método es el método a aplicar y data son los datos que hay
# que pasar para el funcionamiento del método (si es que se requieren)

palabras = "Estas son palabras"

# Al utilizar el método upper, el contenido de la variable se convierte en mayúsculas
print(palabras.upper())  # >ESTAS SON PALABRAS

# Al utilizar el método lower, el contenido de la variable se convierte en minúsculas
print(palabras.lower())  # >estas son palabras

# Al utilizar el método find, nos devuelve el número de índice donde comienza la cadena buscada
print(palabras.find('son'))  # >6

# Replace reemplaza la cadena buscada, con la cadena entregada
print(palabras.replace('son', 'no son'))  # >Estas no son palabras

# Split separa la cadena en una lista. Por defecto, si no se entrega ningún separador, separará en un espacio.
lista = palabras.split()
print(lista)  # >['Estas', 'son', 'palabras']
print(type(lista))  # ><class 'list'>

# Join une la lista con el elemento entregado, en este caso una coma
print(",".join(lista))  # >Estas,son,palabras

# Propiedades de los strings
# Los strings son INMUTABLES
# Los strings son CONCATENABLES y OPERABLES
# Los strings son MULTILINEALES
# Los strings son VERIFICABLES
# Los strings son MEDIBLES

# Otros tipos de datos

# LISTAS
# Las listas son un conjunto de objetos. Pueden contener cualquier tipo de dato dentro, incluso otras listas:
lista1 = ["Hola", "mundo", 3, 2563, [1, 2]]
print(lista1)  # >["Hola", "mundo", 3, 2563, [1, 2]]
print(type(lista1))  # ><class 'list'>

# Todas las listas tienen un índice que comienza en 0 y sirve para llamar o ubicar los elementos:
# ["Hola", "mundo", 3, 2563, [1, 2]]
#    0        1     2    3      4
# Se pueden utilizar los índices para llamar o reemplazar los elementos de la lista:
print(lista1[1])  # >'mundo'
print(lista1[2])  # >3
print(lista1[3])  # >2563
print(lista1[4])  # >[1, 2]
print(lista1[4][0])  # >1

# Reemplazando la palabra "Hola" por "Adios"
lista1[0] = "Adiós"
print(lista1)  # >["Adiós", "mundo", 3, 2563, [1, 2]]

# Métodos de las listas:
lista1.append("Nuevo elemento")  # para agregar un elemento a una lista se utiliza el método append
print(lista1)  # >["Adiós", "mundo", 3, 2563, [1, 2], "Nuevo elemento"]

variable = lista1.pop(1)
print(lista1)  # >["Adiós", 3, 2563, [1, 2], "Nuevo elemento"]
print(variable) # >'mundo'

lista1.remove(3)
print(lista1) # >["Adiós", 2563, [1, 2], "Nuevo elemento"]


# Prueba los siguientes métodos y revisa el efecto que tienen en las listas!
# lista1.sort()
# lista1.count()
# lista1.reverse()


# DICCIONARIOS
#Los diccionarios son un conjunto de objetos que se encuentran conformados por pares 'llave' y 'valor'.
#Los diccionarios NO son indexables

dic = {1: "hola", 2: "mundo", "llave": "valor", "lista": [1, 2, 3]}

print(dic) # >{1: 'hola', 2: 'mundo', 'llave': 'valor', 'lista': [1, 2, 3]}

print(type(dic)) # ><class 'dict'>

print(dic["llave"]) # >'valor'

print(dic["lista"][1]) # >2

dic.update({10: "valor", 20: "veinte"})  # Podemos agregar valores al diccionario utilizando el método update

print(dic) # >{1: 'hola', 2: 'mundo', 'llave': 'valor', 'lista': [1, 2, 3], 10: 'valor', 20: 'veinte'}

# Prueba estos métodos y revisa qué efecto tienen sobre un diccionario:
# dic.keys()
# dic.values()
# dic.pop()
# dic.items()
# del dic[20]
# dic.clear()

# TUPLES
print("Los tuples son listas de elementos que NO pueden ser alterados o modificados de ninguna manera")
tup = (1, 5, "hola", "mundo")
print(tup)
print(type(tup))
print(tup[2])
# Si bien las tuplas tienen algunos métodos, la mayor utilidad que tienen es que son inmutables,
# además de su función de empacar y desempacar

# SETS
#Los sets son listas de elementos que no pueden estar duplicados

mi_set = {7, 2, 4, "zebra", "hola", "mundo", "mundo"}

print(mi_set) # >{2, 'mundo', 4, '23', 7, 'zebra', 'hola'}

print(type(mi_set)) # ><class 'set'>

#Pasar un elemento duplicado al set mantendrá solo una de las copias del elemento:

mi_set.add(1)
mi_set.add(1)
mi_set.add(1)

print(mi_set) # >{1, 2, 'mundo', 4, '23', 7, 'zebra', 'hola'}

#Intenta remover datos del set usando el método remove()


# BOOLEANO
#Los booleanos son la base de la programación y se utilizan para hacer flags. Son solo True y False
bol = True
print(bol) # >True
print(type(bol)) # ><class 'bool'>


# Actividades

#01

'''
Crea un programa que le pida al usuario que ingrese un texto
El algoritmo debe guardar este texto en una variable
El algoritmo debe analizar el texto y mostrar en pantalla:

- La cantidad de veces que aparece la letra 'a',
- La cantidad de veces que aparece la palabra 'de',
- La cantidad de letras que tiene el texto,
- La cantidad de palabras que tiene el texto,
- Una lista con todas las palabras que tenga el texto,
- La lista en orden inverso,
- El texto en orden inverso.
'''

