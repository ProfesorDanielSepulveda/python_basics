'''Contadores, Banderas, Acumuladores
'''

# Contadores, Acumuladores y Banderas
# Los contadores y acumuladores son variables que nos permiten llevar la cuenta de algunas cosas.
# Un contador lleva la cuenta de una acción, un ciclo o una cantidad de eventos.
# Generalmente, un contador comienza en 0 y se le suma 1 por cada acción.
# El objetivo del contador es establecer un límite, desencadenar un evento o simplemente saber cuántas veces ocurre algo.
# Un acumulador es una variable capaz de llevar la cuenta de cantidades que pueden variar.
# Un acumulador sirve para medir la cantidad de dinero, unidades o existencias de algún elemento.
# Por otro lado, una bandera es una variable que contiene un booleano True o False.
# El objetivo de este booleano es actuar como semáforo para permitir un determinado evento o no.

# Ejemplo de uso de contadores, acumuladores y banderas

#01
haberes = 357000000
cuenta = 800000000
bandera = False

print(f"Antes del giro, el estado de la bandera es {bandera} y el saldo en la cuenta es de ${cuenta}")

if not bandera:
    cuenta -= haberes
    bandera = True

print(f"Después del giro, el estado de la bandera es {bandera} y el saldo en la cuenta es de ${cuenta}")

#02
contador = 0

print(f"Antes de la operación, el numero del contador es {contador}")

if contador > 5:
    print("El estudiante no puede tomar prestado un libro, ya está en el tope máximo permitido")
else:
    print(f"El estudiante tiene {contador} libros prestados, puede tomar uno más")
    contador += 1

print(f"Después de la operación, el numero del contador es {contador}")

# Ejercicios:

#01
# Generamos un programa que pida al usuario que controle un sistema de retiros del banco "Quisquillosos".
# El banco permite un total de hasta 3 depósitos por mes, luego no permite realizar más depósitos.
# El banco permite retiros solo si el monto en la cuenta supera la cantidad de 1.000.000 o si el cliente tiene acceso especial.

#02
#Genera un algoritmo que pida al usuario una cancion y su año de lanzamiento.
#Luego, si la canción es del año 2000 o anterior, guardala en un diccionario.
#Si la canción es del año 2001 o más reciente, guarda en una lista llamada anios el año
#y en otra lista llamada canciones la cancion
#Despliéga en pantalla la infomración de la cancion con el formato:

#'La cancion {cancion} fue lanzada en el año {anio}'

#asegurate de que el algoritmo BORRE los datos dentro de las listas o diccionario
#segun corresponda y luego imprime estas variables en pantalla para confirmar la operacion
#Manten una cuenta de cada ingreso de texto que el usuario realiza en una variable llamada contador
#al final del algoritmo imprime la variable contador con el siguiente formato:

#'El usuario ingresó texto {contador} veces'
