import numpy as np

#Dados los siguientes dos arrays construidos de forma manual:


array1 = np.array([[1, 1, 1, 1, 1],
                   [2, 2, 2, 2, 2],
                   [3, 3, 3, 3, 3],
                   [4, 4, 4, 4, 4]])


array2 = np.array([[2, 2, 2, 2, 2],
                   [3, 3, 3, 3, 3],
                   [4, 4, 4, 4, 4],
                   [5, 5, 5, 5, 5]])


#Vamos a realizar algunas operaciones sencillas con los array.
#Sumarlos:
print(array1 + array2)

#Restarlos
print(array1 - array2)

#Multiplicarlos
print(array1 * array2)

#Elevarlos al cuadrado
print(array1 ** 2)
print(array2 ** 2)


#Sacarles raíz cuadrada
print(array1 ** 0.5)
print(array2 ** 0.5)


#Obtener media o promedio
print(array1.mean())
print(array2.mean())

#Obtener máximo
print(array1.max())
print(array2.max())

#Obtener mínimo
print(array1.min())
print(array2.min())

#Realizar comparaciones lógicas entre ellos
print(array1 < array2)

#Filtrart sus valores
print(array1 < 3)
print(array2 < 3)

#Ordenarlos

array1 = np.random.randint(0,21,(5,5))

print(array1)
'''
[[ 2 18  5 13 19]
 [ 7 20  4  2 19]
 [ 6 12 20 11 11]
 [15 19  7  5 11]
 [ 4 18 15 10 19]]
'''

'''
print(np.sort(array1))
[[ 2  5 13 18 19]
 [ 2  4  7 19 20]
 [ 6 11 11 12 20]
 [ 5  7 11 15 19]
 [ 4 10 15 18 19]]
'''


#Los arrays pueden ser transformados para alterar sus formas y para transponer sus datos:
#En este caso de ejemplo, trabajaremos con un array generado de forma manual:

ejemplo = np.array([[1, 2, 3, 4,  5],
                    [6, 7, 8, 9, 10]])

print(ejemplo)
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
'''

#Actualmente la forma de este array de dos dimensiones es de 2, 5
#Vamos a transformarlo para convertirlo en un array 5, 2

print(ejemplo.reshape(5, 2))
'''
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]]
'''

#Eso no significa que la forma haya cambiado, puesto que solo lo arrojamos a un print.
#La forma original del array sigue siendo la misma:
print(ejemplo)
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
'''

#Para que efectivamente la forma cambie, debemos guardarlo en la variable:

ejemplo = ejemplo.reshape(5, 2)
print(ejemplo)
'''
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]]
'''

#Los arrays pueden transponerse, esto quiere decir:
#cambiar lo de las filas a las columnas y lo de las columnas a las filas
#Para este ejemplo trabajaremos con el array creado de forma manual:

array1 = np.array([[1, 1, 1, 1, 1],
                   [2, 2, 2, 2, 2],
                   [3, 3, 3, 3, 3],
                   [4, 4, 4, 4, 4]])

print(array1)
'''
[[1 1 1 1 1]
 [2 2 2 2 2]
 [3 3 3 3 3]
 [4 4 4 4 4]]
'''

print(array1.T)
'''
[[1 2 3 4]
 [1 2 3 4]
 [1 2 3 4]
 [1 2 3 4]
 [1 2 3 4]]
'''


#A través de Numpy, podemos generar arreglos rápidamente para manejar grandes cantidades de datos.
#Por ejemplo, si quisiera generar los asientos de un cine con diez salas, podría generar rápidamente estos datos a través de numpy y sus métodos.

matriz = np.arange(1,1001).reshape(10,10,10)
print(matriz)
'''
[[[   1    2    3    4    5    6    7    8    9   10]
  [  11   12   13   14   15   16   17   18   19   20]
  [  21   22   23   24   25   26   27   28   29   30]
  [  31   32   33   34   35   36   37   38   39   40]
  [  41   42   43   44   45   46   47   48   49   50]
  [  51   52   53   54   55   56   57   58   59   60]
  [  61   62   63   64   65   66   67   68   69   70]
  [  71   72   73   74   75   76   77   78   79   80]
  [  81   82   83   84   85   86   87   88   89   90]
  [  91   92   93   94   95   96   97   98   99  100]]

 ...

 [[ 901  902  903  904  905  906  907  908  909  910]
  [ 911  912  913  914  915  916  917  918  919  920]
  [ 921  922  923  924  925  926  927  928  929  930]
  [ 931  932  933  934  935  936  937  938  939  940]
  [ 941  942  943  944  945  946  947  948  949  950]
  [ 951  952  953  954  955  956  957  958  959  960]
  [ 961  962  963  964  965  966  967  968  969  970]
  [ 971  972  973  974  975  976  977  978  979  980]
  [ 981  982  983  984  985  986  987  988  989  990]
  [ 991  992  993  994  995  996  997  998  999 1000]]]
'''

#Si quisiera hacer lo mismo, pero reemplazando la matriz con datos pequeños para luego comenzar a insertar los datos,
#entonces podría generar una matriz en blanco con "unos"

matriz = np.ones((10,10), dtype = np.int8)
print(matriz)
'''
[[1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]
 [1 1 1 1 1 1 1 1 1 1]]
'''

#arange genera rangos rápidamente, sin embargo, lo que realmente se utiliza para generar secuencias es linspace
#linspace genera automaticamente secuencias con los datos (inicio, final, cantidad)
#linspace es muy importante a la hora de trabajar con otros módulos y es una de las principales bases para construir machine learning

#En este caso linspace genera un arreglo de 20 números entre el 10 y el 20 (incluyendo inicio y final)
matriz = np.linspace(10,20,21)
print(matriz)
'''
[10.  10.5 11.  11.5 12.  12.5 13.  13.5 14.  14.5 15.  15.5 16.  16.5
 17.  17.5 18.  18.5 19.  19.5 20. ]
'''

#Luego, generamos un segundo arreglo de 20 números entre el 30 y el 40
base = np.linspace(30,40,21)
print(base)
'''
[30.  30.5 31.  31.5 32.  32.5 33.  33.5 34.  34.5 35.  35.5 36.  36.5
 37.  37.5 38.  38.5 39.  39.5 40. ]
'''

#Finalmente, ahora que tenemos dos arreglos, podemos hacer operaciones más complejas, como por ejemplo concatenar:
arr = np.concatenate((matriz,base))
print(arr)
'''
[10.  10.5 11.  11.5 12.  12.5 13.  13.5 14.  14.5 15.  15.5 16.  16.5
 17.  17.5 18.  18.5 19.  19.5 20.  30.  30.5 31.  31.5 32.  32.5 33.
 33.5 34.  34.5 35.  35.5 36.  36.5 37.  37.5 38.  38.5 39.  39.5 40. ]
'''

#Finalmente, Numpy permite la generación de números aleatorios también a través de la librería random con una variante de rango.
#Esta generación aleatoria permite generar números aleatorios a través de una semilla, lo que es parte de la base para el trabajo de redes neuronales.

#Vamos a generar una matriz a través de un rango default usando la semilla 2
matriz = np.random.default_rng(2)

#Luego vamos a generar 100 números aleatorios a partir de esto:
base = matriz.random(100)
print(base)
'''
[0.26161213 0.29849114 0.81422574 0.09191594 0.60010053 0.72856053
 0.18790107 0.05514663 0.27496937 0.65743301 0.56226566 0.15006226
 0.43263079 0.6692973  0.42278467 0.6331844  0.96743595 0.68306482
 0.39162483 0.18725257 0.34596067 0.51106597 0.89120941 0.77556394
 0.3181466  0.9242169  0.47090989 0.69375884 0.10720731 0.10454356
 0.20190745 0.88444967 0.67981146 0.84923632 0.64443627 0.4065424
 0.51657819 0.59344352 0.86211798 0.43818617 0.89224011 0.61371694
 0.82935613 0.49805605 0.69251813 0.33902537 0.5228285  0.21622339
 0.1007036  0.03860413 0.70194948 0.45643062 0.89773415 0.8351832
 0.38509513 0.97367877 0.59206201 0.76588331 0.40719436 0.19616991
 0.17177702 0.18120623 0.60380552 0.11263286 0.01991075 0.83299696
 0.09941112 0.45058454 0.48849857 0.62027241 0.50401448 0.93734314
 0.75039659 0.5744665  0.61727214 0.50655149 0.96476181 0.22662606
 0.68902714 0.55509668 0.04201179 0.29615    0.92716694 0.78456486
 0.01283109 0.29662633 0.00980535 0.82746694 0.11036759 0.05745518
 0.98188334 0.44586988 0.318393   0.04901339 0.38959528 0.36603906
 0.52348079 0.00678547 0.14796288 0.20988653]
'''

#Hay más métodos para poder generar números aleatorios y muchas cosas que pueden hacerse con estos objetos generados, pero es material más avanzado.
