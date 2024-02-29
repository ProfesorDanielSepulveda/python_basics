import numpy as np

#En esta clase vamos a trabajar con un arreglo aleatorio.
#Para eso, vamos a construir un generador aleatorio con semilla 2 y luego
#Vamos a generar 100 números aleatorios entre el 1 y el 50:


matriz = np.random.default_rng(2)
base = matriz.integers(50, size = (10,10))

#Como todos trabajaremos con un generador con la misma semilla, entonces todos tendremos el mismo array:

print(base)
'''
[[41 13  5 14 20 40 22  4 16 30]
 [40 36 49  9 44  2 27 13 10 32]
 [15 28 13  7 37 21 33 33 47 21]
 [10 31 46 48 43 34 19 19  1  9]
 [16 17 28 25 34 44 43 38 48 15]
 [45 46 11 23 28 34 35  5 23  5]
 [47 10 22 44 26 33 24 42 29 32]
 [22 20 29 25 39 29 23 43 10 21]
 [24 44 22 30  3 41 22 24  4 34]
 [31 16 38 26  2 10 12  5 25  1]]
'''

#Vamos a trabajar sobre el eje 0 para poder extraer los mínimos de cada columna
#Recuerda siempre: AXIS = 0 significa COLUMNAS
print(base.min(axis = 0))
#> [10 10  5  7  2  2 12  4  1  1]

#Ahora haremos lo mismo con las filas.
#Recuerda siempre: AXIS = 1 significa FILAS
print(base.min(axis = 1))
#> [ 4  2  7  1 15  5 10 10  3  1]

#Vamos a filtrar este arreglo.
#Para poder aplicarle un filtro, vamos a buscar todos los valores que sean menores a 6
#Esto me va a devolver un arreglo de booleanos que me indicará cuales son las coincidencias:

print(base<6)
'''
[[False False  True False False False False  True False False]
 [False False False False False  True False False False False]
 [False False False False False False False False False False]
 [False False False False False False False False  True False]
 [False False False False False False False False False False]
 [False False False False False False False  True False  True]
 [False False False False False False False False False False]
 [False False False False False False False False False False]
 [False False False False  True False False False  True False]
 [False False False False  True False False  True False  True]]
'''

 #Este filtro, desde luego, no es completamente funcional si yo quiero operar los valores.

print(base[base<6])
#> [5 4 2 1 5 5 3 4 2 5 1]

#El resultado es un array unidimensional que contiene todos los valores solicitados y con el cual si puedo operar.
#Haremos algunos ejercicios con este grupo extraído:


# MANIPULACIÓN DE DATOS EN ARRAYS.

#Los datos dentro de los arrays pueden manipularse según las circunstancias de lo que se necesite hacer.
#Es posible manipular y llamar un dato específico en uno de los campos del array.
#Comencemos por un array de un nivel:

arreglo = base[base<6]
print(arreglo)
#> [5 4 2 1 5 5 3 4 2 5 1]

#Debemos recordar que python comienza en índice 0, por tanto, si yo llamo al índice 0, lo que mostrará será un 5:

print(arreglo[0])
#> 5

#Luego, puedo llamar una seccion específica del array, por ejemplo desde el índice 1 (que es 4) hasta el índice 3 (que es 1):

print(arreglo[1:4])
#> [4 2 1]

#también es posible llamar a estos valores con saltos:
#Es este caso llamaremos a los valores desde el índice 0 al 5 cada 2 valores:
print(arreglo[0:5:2])
#> [5 2 5]

#Para editar un valor en un array, simplemente hay que seleccionarlo usando su índice y luego reemplazarlo:
print(arreglo)
#> [5 4 2 1 5 5 3 4 2 5 1]

arreglo[3] = 0
print(arreglo)
#> [5 4 2 0 5 5 3 4 2 5 1]
#         ↑

#Sin embargo, se debe tener en cuenta que la edición de datos podría traer complicaciones si es que no se realiza correctamente.
#Explicación:
#En este caso específico, este array está construído en base a enteros. Todo lo que contiene son números

print(arreglo.dtype)
#> int32

#Si la edición de datos se realizara insertando un STR en vez de un INT, desencadenaría en un error por compatibilidad entre tipo de datos:
arreglo[3] = "a"

'''
Traceback (most recent call last):
  File "C:/Users/LCXX13001XX/Desktop/asd.py", line 9, in <module>
    arreglo[3] = "a"
ValueError: invalid literal for int() with base 10: 'a'
'''

#Esto se debe a que los arreglos deben manejar un tipo de dato unificado.:
test = np.array([0, 0, 0, 0])
print(test.dtype)
#> int32

print(test)
#> [0 0 0 0]

test = np.array(["a", "a", "a", "a"])
print(test.dtype)
#> <U1
print(test)
#> ['a' 'a' 'a' 'a']

test = np.array([True, True, True, True])
print(test.dtype)
#> bool
print(test)
#> [ True  True  True  True]


#Regresemos a la modificación:
#Modificar con : realizará modificaciones masivas:

print(arreglo)
#> [5 4 2 1 5 5 3 4 2 5 1]

arreglo[0:11] = 0
print(arreglo)
#> [0 0 0 0 0 0 0 0 0 0 0]

arreglo[0:11:2] = 1
print(arreglo)
#> [1 4 1 1 1 5 1 4 1 5 1]

#Luego, para poder trabajar en un array de dos dimensiones, debo agregar una dimensión a la localización:
print(base)
'''
[[41 13  5 14 20 40 22  4 16 30]
 [40 36 49  9 44  2 27 13 10 32]
 [15 28 13  7 37 21 33 33 47 21]
 [10 31 46 48 43 34 19 19  1  9]
 [16 17 28 25 34 44 43 38 48 15]
 [45 46 11 23 28 34 35  5 23  5]
 [47 10 22 44 26 33 24 42 29 32]
 [22 20 29 25 39 29 23 43 10 21]
 [24 44 22 30  3 41 22 24  4 34]
 [31 16 38 26  2 10 12  5 25  1]]
  ↑
'''
#Vamos a convertir el número señalado en un 0:

base[9, 0] = 0
print(base)
'''
[[41 13  5 14 20 40 22  4 16 30]
 [40 36 49  9 44  2 27 13 10 32]
 [15 28 13  7 37 21 33 33 47 21]
 [10 31 46 48 43 34 19 19  1  9]
 [16 17 28 25 34 44 43 38 48 15]
 [45 46 11 23 28 34 35  5 23  5]
 [47 10 22 44 26 33 24 42 29 32]
 [22 20 29 25 39 29 23 43 10 21]
 [24 44 22 30  3 41 22 24  4 34]
 [ 0 16 38 26  2 10 12  5 25  1]]
   ↑
'''

#POR CADA NIVEL DEL ARRAY, SE DEBE AGREGAR UN NIVEL A LA LOCALIZACIÓN POR ÍNDICES
#Ejemplo con un array de 3 dimensiones

array = np.array([[[ 1, 2, 3],
                   [ 4, 5, 6]],
                  [[ 7, 8, 9],
                   [10,11,12]]])

#Para poder extraer el número 8 desde este array:
print(array[1, 0, 1])
#> 8


#También es posible manejar las extracciones de datos y manipulaciones directamente por dimensiones.
print(base)
'''
[[41 13  5 14 20 40 22  4 16 30]
 [40 36 49  9 44  2 27 13 10 32]
 [15 28 13  7 37 21 33 33 47 21]
 [10 31 46 48 43 34 19 19  1  9]
 [16 17 28 25 34 44 43 38 48 15]
 [45 46 11 23 28 34 35  5 23  5]
 [47 10 22 44 26 33 24 42 29 32]
 [22 20 29 25 39 29 23 43 10 21]
 [24 44 22 30  3 41 22 24  4 34]
 [31 16 38 26  2 10 12  5 25  1]]
'''

#Vamos a extraer la segunda dimensión de este arreglo de dos dimensiones:
#Esto se puede lograr debido a que la indexación de las dimensiones siempre comienza desde las dimensiones más superiores hacia las más profundas.

print(base[1])
#> [40 36 49  9 44  2 27 13 10 32]

#También podemos extraer una X cantidad de dimensiones
#Por ejemplo aquí están las 4 primeras dimensiones.

print(base[::3])
'''
[[41 13  5 14 20 40 22  4 16 30]
 [10 31 46 48 43 34 19 19  1  9]
 [47 10 22 44 26 33 24 42 29 32]
 [31 16 38 26  2 10 12  5 25  1]]
'''

#De la misma forma, podemos extraer rangos:
print(base[2:5])
'''
[[15 28 13  7 37 21 33 33 47 21]
 [10 31 46 48 43 34 19 19  1  9]
 [16 17 28 25 34 44 43 38 48 15]]
'''

 #Y también podemos extraer porciones completas del array:
print(base[:4,:4])
'''
 [[41 13  5 14]
 [40 36 49  9]
 [15 28 13  7]
 [10 31 46 48]]
'''