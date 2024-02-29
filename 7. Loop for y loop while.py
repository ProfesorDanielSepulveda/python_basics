'''Loop For, Loop While
'''

# Los loops son repeticiones de bucles que nos permiten realizar una acción una determinada cantidad de veces
# o realizarla mientras se cumpla una determinada condición y hasta que esa condición se interrumpa.
# Hay dos tipos de loops en Python: loop for y loop while.
# El loop for genera un ciclo que se repite una determinada cantidad de veces.
# El loop while genera un ciclo que se repite de forma permanente mientras se cumpla una determinada condición.

# Ejemplo de loop for
# 01
print("Ejemplo de loop for:")
for numero in range(1, 6):
    print("Este es un loop que se repite cinco veces")

# 02
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print("Este es un loop que se repite cinco veces")


# Ejemplo de loop while
# 01
print("Ejemplo de loop while:")
bandera = True
contador = 0
while bandera:
    print('Este loop se ejecuta mientras la bandera esté en TRUE y el contador sea igual o menor a 5')
    contador += 1
    if contador >= 5:
        break

# 02
print("Ejemplo de loop while con interacción del usuario:")
bandera = True
while bandera:
    respuesta = input("¿Quieres seguir ejecutando el programa? (s/n): ")
    if respuesta == "n":
        bandera = False

# 03
while True:
    respuesta = input("¿Quieres seguir ejecutando el programa? (s/n): ")
    if respuesta == "n":
        break


# Palabras clave para manejar loops
# continue: interrumpe la iteración actual, pero permite que el loop continue con su funcionamiento normal después
# pass: permite que saltemos el loop si es que aún no lo tenemos terminado o si aún no tenemos claro el funcionamiento.
# break: permite cortar el loop, independiente de cualquier otro factor.


# Ejercicios:

# 01
# Vamos a crear un programa que pida al usuario que ingrese su nombre, su apellido, su año de nacimiento su edad en número.
# validar que el nombre sea en formato alfabetico
# validar que el apellido sea en formato alfabético
# validar que la edad y el año de nacimiento sean en formato numérico
# por la cantidad de años que tenga el usuario, generar una línea que diga "nombre apellido, en el año xxxx cumpliste XX año/s"

#OUTPUT:
"Juanin Juan Harry, en el año 1990 cumpliste 1 año"
"Juanin Juan Harry, en el año 1991 cumpliste 2 años"
"Juanin Juan Harry, en el año 1992 cumpliste 3 años"
"Juanin Juan Harry, en el año 1993 cumpliste 4 años"



# 02
# Crea un algoritmo que contenga dos listas: nombres y apellidos
# Crea un menu que se mantenga activo hasta que el usuario decida terminarlo
# Genera dos opciones: ingresar cliente y ver clientes
# AL ingresar cliente, debe pedir nombre y apellido y agregar estos datos a la lista respectiva
# Al seleccionar ver clientes debe mostrar una lista de los clientes.

# OUTPUT
'''
=====================
====BASE DE DATOS====
=====================

¿Que quieres hacer?

1. Ingresar cliente
2. Ver clientes
3. Salir

>1
Ingresa nombre: NOMBRE
ingresa apellido : APELLIDO

>2
1. Juan Mendoza
2. Estefanía Cardenas
3. Pedro Pérez

>3
Adios!
'''