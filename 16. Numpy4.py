#Aplicaciones NUMPY

import numpy as np

# Vamos a comenzar con un array de diez digitos:
array = np.arange(10)
print(array)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#Este es un array UNIDIMENSIONAL. Si yo quisiera agregar una segunda dimension con los numeros hasta el 190
#Entonces primero necesitaria convertirlo en un array bidimensional
#Hacer eso es bastante sencillo:

array[np.newaxis, :]
print(array)
array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])

#Ahora que tengo el array bidimensional, puedo agregar la segunda hilera de números.
#Una forma de hacerlo sería utilizar el método append (como en las listas)
#Pero es engorroso, poco eficiente y consume más memoria.
#La forma más sencilla de hacerlo es apilar los arrays.

#Primero genero el nuevo array que quiero ingresar abajo del segundo:
new_array = np.arange(10, 20)
print(new_array)
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

#Ahora apilo los arrays:
array = np.vstack((array, new_array))
print(array)
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]])

