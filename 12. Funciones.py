#Funciones. Return. Interacción entre funciones. Funciones Dinámicas. * y **

#Una función permite crear un trozo de código que podemos repetir cuantas veces queramos
#La ventaja de las funciones es que nos permiten realizar acciones con el código sin volver a escribirlo

#Una función se compone de nombre, argumento y cuerpo:
#def NOMBRE_DE_LA_FUNCION(ARGUMENTO):
  #CUERPO DE LA FUNCION

#Cada vez que llamemos a la función por su nombre:
#NOMBRE_DE_LA_FUNCION(ARGUMENTO)
#El cuerpo se ejecutará automáticamente

#Ejemplo:

lista_alumnos = ["Juan", "Carlos", "María", "Estefanía", "Pedro"]

# esta función me permite saludar a los alumnos
def saludar(nombre):
    print(f"Hola, {nombre}, bienvenido a la última unidad del curso de Python")

for alumno in lista_alumnos:
    saludar(alumno)

#Una función puede tener o no tener argumentos
#Es importante al construir funciones, contemplar y considerar con detalle los argumentos que van a utilizarse
#Una cantidad de argumentos incorrecta impedirá que se ejecute la función correctamente
#Hagamos ejemplos de funciones: sin argumentos, con un argumento, con dos argumentos


#Esta es una función sin argumentos:
def funcion_sin_argumentos():
    print("\nAllá en el monte")
    print("Había un charquito")
    print("Se hacía grande")
    print("Se hacía chiquito\n")

print("Les voy a cantar una canción")
#> Les voy a cantar una canción

funcion_sin_argumentos()
#> Allá en el monte
#> Había un charquito
#> Se hacía grande
#> Se hacía chiquito


#Esta es una función con un argumento:
#El argumento de una función sirve para recibir un valor.
#Cuando se le pasa un argumento, la función reemplaza el valor dado en el cuerpo de la función:

lista = ["marcos", "felipe", "juan", "esteban", "maria", "estefania"]

def manzana(a):
    print(f"{a} se está comiendo una manzana")

def pera(a):
    print(f"Ahora {a} se está comiendo una pera")

for i in lista:
    manzana(i)
    pera(i)

pera("pepito")


#Ahora veamos un ejemplo de funciones con dos argumentos:

def generador(nombre,empresa):
    rut = input(f"Por favor, ingresa el rut de {nombre}")
    print(f"{nombre}, con rut {rut}, trabaja en {empresa}")

generador("Carlos", "DUOC")
generador("Marcela", "DUOC")


#return permite que la función nos devuelva un resultado
#Este resultado es compatible con palabras clave, métodos y podemos almacenarlo en variables.
#La presencia de un return interrumpe la función y la termina inmediatamente.
#Return puede devolver uno o varios valores al mismo tiempo
#Hagamos funciones con return!


#El uso de return es importante porque las funciones están formadas por lo que se llama
#"Ambiente local"
#Una función se encuentra, en cierto modo, aislada del resto del código,
#De modo que la función, puede acceder (y solo acceder) a variables y parámetros que se encuentren fuera de ella,
#Pero el resto del código no puede acceder a las variables y parámetros dentro de la función,
#A menos que devolvamos estos valores con un return
#De este modo, el código fuera de las funciones se define como "local"
#Y el código fuera de las funciones se define como global

def sumar(sumando1, sumando2):
	#sumando1, sumando2 y suma son variables locales que corresponden al ámbito local de la función sumar
    #Posteriormente, la variable suma se extrae desde el ambiente local a través del return
	suma = sumando1 + sumando2
	return suma

print(sumar(4, 5))

#Intentar llamar una variable local desde el ambiente global derivará en un error:
#El namerror indica que la variable no está definida:

def funcion():
    variable = "Esta es una variable local"
    print(variable)

#En este caso, llamar la variable desde fuera de la función desencadenará un error.
#Esto se debe a que la variable es LOCAL, solo existe dentro de la función
#Una vez acaba la función, la variable deja de existir.
print(variable)
"""
Traceback (most recent call last):
  File "D:\PYTHON\testing.py", line 6, in <module>
    print(variable)
NameError: name 'variable' is not defined
"""

#Las variables globales pueden ser llamadas desde cualquier sitio, incluso dentro de funciones.
def nadar():
    print(f"el {animal} nada")

animal = "cocodrilo"
nadar()


#Una cosa es que las variables globales sean accesibles desde los ambientes locales,
#Es decir, que una función pueda acceder a las variables que hay fuera de ella
#Pero otra muy distinta es que una función pueda modificarlas.
#Atentos con este ejemplo:

#Tengo una variable que me declara un animal:
animal = "elefante"

#Tengo una función que cambia el animal por otro.
def cambiar_animal():
    animal = "ratón"

#Vamos a verificar el valor de la variable "animal" antes y después de ejecutar la función.
print(f"El animal es un {animal}")
#> El animal es un elefante

cambiar_animal()

print(f"El animal es un {animal}")
#> El animal es un elefante

#Esto se hace para proteger las variables globales de modificaciones accidentales.
#Para poder hacer modificaciones a variables globales en ambientes locales, debemos usar el comando "global"

animal = "cocodrilo"
def cambiar_animal():
    global animal
    animal = "ratón"


print(f"El animal es un {animal}")
#> El animal es un cocodrilo

cambiar_animal()

print(f"El animal es un {animal}")
#> El animal es un ratón

#De esta forma, cuando tenemos variables con el mismo nombre en el ambito global y local
#Pero usamos el comando "global",
#Le estamos diciendo a Python que estamos usando la variable del ambiente global.
#Pero ¿Y si no es asi?
#Entonces tenemos un conflicto, porque tenemos dos variables independientes que ocupan el mismo nombre:
#Una en ambiente global y una em ambiente local:

variable = "Esta variable es del ambiente global"

def otra_funcion():
    variable = "Esta variable es del ambiente local"
    print(variable)

print(variable)
#> 'Esta variable es del ambiente global'

otra_funcion()
#> 'Esta variable es del ambiente local'

#El hecho de tener funciones con nombres identicos en ambiente local y global puede conducir a errores:
#Se recomienda que los nombres de las variables locales sean idénticos a los de variables globales solo si van a referenciarlas
#Para lo cual se debe complementar con el comando "global"
#No generar la referencia derivará en un error:

variable = "elefante"

def cambio():
	print(f"el animal es un {variable}")
	variable = "ratón"
	print(f"el animal es un {variable}")

cambio()


#Un problema similar tendremos si
#intentamos acceder variables que comparten un mismo nombre en funciones dentro de funciones:

#En este caso: hay una función dentro de una función, en ambas existe una variable "valor"
#Pero, en cada una de ellas, la variable es local, por lo que son en realidad, variables independientes dentro de ambientes locales independientes.

def funcion_padre():
	valor = 10

	def funcion_anidada():
		valor = 20
		print(f'Valor en función anidada es {valor}')

	print(f'Valor en función padre antes es {valor}')
	funcion_anidada()
	print(f'Valor en función padre después es {valor}')

funcion_padre()

#Es posible indicarle a python que las variables no harán referencia a variables globales,
#Pero que si a variables con el mismo nombre dentro de otras funciones, utilizando el comando "nonlocal"

def funcion_padre():
	valor = 10

	def funcion_anidada():
		nonlocal valor
		valor = 20
		print(f'Valor en función anidada es {valor}')

	print(f'Valor en función padre antes es {valor}')
	funcion_anidada()
	print(f'Valor en función padre después es {valor}')

funcion_padre()


#Las funciones pueden ser dinámicas: lo que quiere decir que el argumento de una función puede ser otra función
#Probemos las funciones dinámicas!!!

def pedir_nombre():
    nombre = input("Por favor, ingresa el nombre: ")
    return nombre

def comer(a):
    print(f"{a} se está comiendo su comida")

comer(pedir_nombre())


#Es importante para esto que la función que se encuentra a mayor nivel de profundidad devuelva valor si es que la función que está más arriba necesita un valor para ejecutarse.


# ARGS

#En ocasiones, no estamos seguros o no sabemos cuantos argumentos van a formar parte de una función
#puesto que, por ejemplo, no sabemos si el usuario pasará uno, dos o más argumentos.
#Para este tipo de situaciones existe la palabra clave *args, que permite que se puedan ingresar múltiples argumentos
#dentro de una función, cada uno como una variable independiente.

#Bajo esta misma línea, también disponemos de la palabra clave **kwargs, que nos permite capturar elementos
#bajo la dinámica 'clave' y 'valor' para así construir diccionarios que se pueden utilizar en la función.

#Utilicemos estas palabras claves para construir funciones con argumentos indeterminados!!!!!!

def menu(*args):
    for index, arg in enumerate(args):
        print(f"{index+1}. {arg}")

menu("Mostrar opciones", "Salir")



def concatenar(**kwargs):
    palabra = ""
    for arg in kwargs.values():
        palabra += arg
    return palabra

print(concatenar(a="H", b="o", c="l", d="a", e="!"))



#Ejercicio:
#Construye un programa que ofrezca las siguientes opciones:
#1. Ingresar información (nombre y rut para guardarlos en listas)
#2. Llamar información (desde las listas, usando indices)
#3. Salir (Del programa)
# CONSTRUYE TODO USANDO FUNCIONES


