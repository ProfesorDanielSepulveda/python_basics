import numpy as np

#Un array es una colección de datos ordenada en filas y columnas.
#Un array tiene tres tipos distintos de dimensiones:
#profundidad, ancho y alto:
#Estas medidas nos permiten ordenar los datos dentro del array.

#<---------> Ancho

#^
#|
#|  Alto
#|
#v

#[1, 2, 3, 4]
#    [5, 6, 7, 8]    Profundidad

#Existen varias formas de generar un array
#La primera de ellas que vamos a explorar es simplemente declararlo
#Ingresando los objetos dentro del array
#Para este efecto, los objetos del array se declaran en una lista, dentro del objeto
#Los array pueden tener una o más dimensiones, declararemos un array unidimensional:

array_uni = np.array([1, 2, 3, 4, 5])
print(array_uni) #> [1 2 3 4 5]
#Esta es la visualización de este array unidimensional que está formado por los números del 1 al 5

print(type(array_uni)) #> <class 'numpy.ndarray'>

#Tal como se puede apreciar, el tipo de dato al que corresponde este objeto es "ndarray"


#Este array es un array unidimensional, puesto que solo tiene una dimension: ancho
#podemos revisar los atributos de este array a través de los siguientes métodos:

print(array_uni.shape) #> (5,)

#Me muestra la forma del array, organizada en alto, ancho, profundo.
#En este caso, como solo tenemos una dimensión, solo nos muestra la dimensión existente (ancho)

print(array_uni.ndim) #> 1
#Nos muestra la cantidad de dimensiones que tiene este array.

print(array_uni.size) #> 5
#Nos muestra el tamaño del array, indicando la cantidad de datos que hay en su interior.


#Al momento de crear el array, podríamos ordenarlo de numerosas formas,"
#Sin embargo, si solo le damos una dimensión, el resultado será siempre un array unidimensional

array_uni = np.array([1,
                      2,
                      3,
                      4,
                      5])

print(array_uni) #> [1 2 3 4 5]

#EJERCICIO!!!!!!!!!!
#Crea un array de una dimensión y compartelo con tu compañero
#tu compañero extraerá de él los datos provenientes de sus métodos.
#Comparen los resultados.

#intenta pensar: ¿Cómo sería un array de dos dimensiones?:

array_bid = np.array([[1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 10]])

print(array_bid)
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
'''

#Este array tiene dos dimensiones: ancho y alto.
#En un array, cada fila de la dimensión de alto se declara dentro de corchetes []
#Luego, todas las filas del array deberán encerrarse dentro de un segundo corchete []
#Esto debido a que para el array, debemos declarar solo un objeto.
#Revisemos los atributos del array bidimensional

print(array_bid.shape)
#> (2, 5)
#2 de alto y 5 de ancho es la forma que tiene este array

print(array_bid.ndim)
#> 2
#El array tiene 2 dimensiones (alto y ancho)

print(array_bid.size)
#> 10
#hay un total de 10 elementos en el interior del array

print(type(array_bid))
#> <class 'numpy.ndarray'>


#Podemos directamente crear un array bidimensional a través de algunos métodos,
#Como por ejemplo 'ones' que nos creará un array con la forma que le insertemos en el formato 'alto, ancho' utilizando números 1
unos = np.ones((4, 3))
print(unos)
'''
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
'''

#Por su parte, el método 'zeros' hace lo propio con números 0
ceros = np.zeros((4, 3))
print(ceros)
'''
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''

 #ES IMPORTANTE TENER EN CONSIDERACIÓN QUE LOS MÉTODOS EXPLICADOS AQUÍ ARRIBA CREAN 1 Y 0
 #EN FORMATO FLOAT, ES DECIR, CADA UNO DE ESTOS DIGITOS ES UN 1.0 O UN 0.0

#El método 'arange' nos permite crear directamente un array a partir de ciertos parámtros
#Para ello se vale de un 'valor inicio, valor final, saltos'
#ES IMPORTANTE TENER EN CUENTA QUE EL ÚLTIMO NÚMERO DE LA SECUENCIA NO SE CONSIDERA
#Es este caso de ejemplo, se está creando un array con los valores del 0 al 100 cada 5 digitos:

array_1 = np.arange(0, 100, 5)
print(array_1)
#> [0  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]

#Y en este otro, se está crando un array con los números del 0 al 10
array_2 = np.arange(0, 10)
print(array_2)
#> [0 1 2 3 4 5 6 7 8 9]

#El resultado será un arreglo unidimensional con los valores ingresados.

#Numpy incluye la liberiría random, de modo que podemos utilizar sus métodos para generar arrays
#En este caso, se usa randint para generar un array con números aleatorios entre el 0 y el 10
#La forma del array será 2 de alto y 5 de ancho

array_2 = np.random.randint(0, 10, (2, 5))
print(array_2)

#Luego, cada vez que este array se genere, tendrá datos distintos en su interior.
'''
[[2 0 5 2 2]
 [7 3 9 1 1]]
'''

print(array_2)
'''
[[8 9 4 1 7]
 [2 6 4 6 7]]
'''


#Es posible también crear el mismo tipo de estructura usando flotantes entre 0 y 1

array_3 = np.random.random((3, 5))
print(array_3)

'''
[[0.01120666 0.91480216 0.03197316 0.01666476 0.0259376 ]
 [0.91079831 0.8592998  0.17991772 0.01267843 0.34321165]
 [0.95655719 0.12129734 0.61087812 0.52297964 0.16304134]]
 '''


#A través del método unique, podemos extraer los valores únicos de un array
#El resultado es un array unidimensional formado por los valores únicos:
array_prueba = np.random.randint(1, 20, (4, 5))
print(array_prueba)

'''
[[12 18 14  0 19  8 17  4 12 11]
 [16 14 16  0 19  7 13  1  5 19]
 [15 14 17  8  6 15 18 15 18  4]
 [ 4 10  8 14 19 11  5 19  0 18]]
'''

print(np.unique(array_prueba))
#> [ 0  1  4  5  6  7  8 10 11 12 13 14 15 16 17 18 19]



