"""Intro: comandos, tipos de datos. String. Print. Input
"""

#Python es un lenguaje de programación que contiene, entre otros elementos, comandos
#(también llamados palabras claves) y variables.
#Los comandos o palabras clave se escriben en inglés y generalmente
#van seguidos de un paréntesis en el cual se inserta la información necesaria para el funcionamiento del comando.
#Por ejemplo: print, cuya función es arrojar cosas a la pantalla para mostrarlas

print("Hola Mundo") #> Hola Mundo


# strings y enteros:

# strings
#Un string o cadena de texto es un conjunto de caracteres.
#Se almacenan entre comillas simples o dobles
#A continuación, veremos algunos string arrojados a la pantalla con print:

print('Esto es texto') #> Esto es texto

print("Casi todo lo que se sitúa entre comillas es texto") #> Casi todo lo que se sitúa entre comillas es texto

print('123456+123456') #> 123456+123456

#Cada una de estas operaciones ha arrojado texto a la pantalla.
#Sabemos que es texto porque está entre comillas,
#Pero también podríamos llamar su tipo de dato a través de la función TYPE
#Para esto es importante entender que, al utilizar una palabra clave como print,
#se le debe entregar un argumento:

#print(argumento)

#El argumento es lo que print arrojará a la pantalla.
#Type es otro tipo de comando, su función es mostrarnos el tipo de dato de su argumento

type('texto') #> <class 'str'>

#str = string = cadena de texto
#La gran mayoría de los comandos en python pueden recibir otros comandos como argumento
#Por ejemplo

print('esto es texto o str') #> esto es texto o str

type(print('esto es texto o str')) #> <class 'str'>

#Print imprime o muestra en pantalla el valor de lo que haya en el argumento
#Si lo que hay en el argumento se encuentra entre comillas dobles o simples:
#Comillas dobles: " "
#comillas simples: ' '
#Entonces print manipulará el elemento como si fuera un string
#Si lo que hay en interior de la palabra clave son 'números', entonces python los tratará como números:
#print también permite imprimir comandos y saltos de líneas,
#Un salto de línea se imprime con \n

print("\n")


print("\nHola Mundo")

#> Hola Mundo

#Imprimamos un string
print("Esto es una cadena o string") #> Esto es una cadena o string

#Ahora imprimiremos un número
print(123456) #> 123456

#Algunos ejemplos de print:
print('1+1') #> 1+1

print(1+1) #> 2

print('Hola' + 'Mundo') #> HolaMundo

print('Hola' + ' ' + 'Mundo') #> Hola Mundo

print('Hola Mundo' + 5)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
'''

#la palabra clave input() nos permitirá ofrecer al usuario la opción de ingresar texto en la consola
#podemos utilizarla de diversas formas:

#Esto no devolverá nada a la pantalla, puesto que es un input, que pide datos
#Pero luego con estos datos no hacemos nada:
input("dime tu nombre: ")


#Esto es un input encerrado dentro de un print, por tanto primero pide datos y luego los devuelve a la pantalla
print(input("dime tu nombre: "))
#> dime tu nombre: Juanin
#>Juanin

#Es es un string unido a un input a través de un proceso llamado concatenación
#Concatenar consiste en "sumar" una cadena a otra (Ojo con los espacios)
#Primero saltará el ínput y luego el print:
#Esto ocurre porque, para que print pueda devolver el valor hacia la pantalla
#primero necesita el valor que se está pidiendo con el input
#Este razonamiento lógico se puede aplicar a casi todos los casos en los
#que se utilizan comandos dentro de comandos

print("tu nombre es " + input("dime tu nombre: "))
#> dime tu nombre: Juanin
#>tu nombre es Juanin

#Aquí hay un proceso de concatenación más extenso
print("Tu nombre es " + input("Dime tu nombre: ") + ". " + "Y tu apellido es" + " " + input("Dime tu apellido: "))
#> dime tu nombre: Juanin
#> dime tu apellido: Juan Harry
#>Tu nombre es Juanin. Y tu apellido es Juan Harry

#La palabra clave 'print', también permite imprimir algunas órdenes básicas anteponiendo un backslash > \ <
#Por ejemplo \n -> Esto imprime un salto de línea
#"por ejemplo \t -> Esto imprime una tabulación

#EJERCICIOS:

#Arma esta cabecera usando una sola línea:

'''
============================
=========BIENVENIDO=========
============================
'''

#Arma este output usando una o varias líneas
'''
Nombre: Raúl
Apellido: Faúndez
Cargo: Electricista
'''

#Genera UNA linea de python que pida nombre, apellido y carrera y arme el siguiente output:
'''
Nombre: NOMBRE
Apellido : APELLIDO
Carrera: CARRERA
¡Bienvenido a Duoc!
'''