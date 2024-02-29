             # generar un programa que capte los siguientes datos de un paciente
# nombre, temperatura, presion (que los pida en una variable, y luego la divida en 2), lesiones graves (s/n)
# que de acuerdo a estas variables:
# si el paciente no cumple con ninguna de las condiciones, lo clasifique como paciente de prioridad baja
# si el paciente cumple con solo algunas de las condiciones, lo clasifique como paciente que requiere atención rapida
# si el paciente tiene las tres condiciones lo clasifique como urgencia médica

#OUTPUTS GUIAS:

'''
=============================
==========URGENCIAS==========
=============================

Ingrese nombre : NOMBRE
Ingrese temperatura: TEMPERATURA
Ingrese presion: XX,XX
Tiene lesiones graves : S/N

El/la paciente {p_nom} no tiene un estado grave, su prioridad de atención es baja
El/la paciente {p_nom} tiene un estado grave, debe ser atendido inmediatamente
El/la paciente {p_nom} tiene un estado que requiere atención rápida.

'''


# Proyecto:

# vamos a crear un programa que nos permita crear un personaje para un videojuego de rol.
# el programa debe comenzar captando el nombre del jugador.
# Un personaje se compone de nombre, raza, edad, fuerza, agilidad, destreza, defensa, magia.
# el programa debe ofrecer al jugador la opción de ingresar un nombre.
# el programa debe preguntar al jugar la raza y edad del personaje.

# el programa debe dar al jugador un total de 30 puntos para repartir entre sus atributos de fz, agi y dez.
# si la cantidad de puntos repartidos no es correcta entonces debe indicarlo y terminar el programa.
# la defensa del personaje debe ser igual a la raiz cuadrada de la agilidad por la destreza, redondeada hacia abajo.
# la magia debe ser igual a la suma de todos los atributos que sean pares dividida por dos.

# Cada raza debe entregar un penalizador de -2 a un atributo a elección y de +5 a un atributo a elección.
# Cada raza debe tener una regla de edades que debe tener una tabla de bonos y penalizaciones. Por ejemplo:
# Humano: si es menor a 20 años, tiene un bonus de +5 en destreza. Si es mayor a 40 años, tiene un penalizador de -5 en defensa
# Cada raza debe tener una tabla de penalizadores distinta.

# Lleva la cuenta de cuantas respuestas ingresó el usuario y cuales fueron los valores que digitó
# Agrega un flag que comience en Flase y cambie a True si la defensa del personaje es inferior a un valor de 10.
# Si el flag es True, al finalizarse el programa debe imprimir un mensaje que diga que el personaje no es muy resistente.
# Muestra cuantas respuestas ingresó el usuario y cuales fueron. Muestra la configuración final del personaje

#OUTPUTS GUIAS:

'''
====================
====JUEGO DE ROL====
====================

INGRESA TU NOMBRE : NOMBRE

Ingresa nombre del personaje:
Ingresa raza del personaje:
Ingresa edad del personaje:

Tienes 30 puntos para repartir entre atributos de fuerzaz, agilidad y destreza:

Ingresa fuerza del personaje:
Ingresa agilidad del personaje:
Ingresa destreza del personaje:

>Los puntos repartidos no son correctos, inicia de nuevo!
>Los puntos repartidos son correctos, puedes continuar!



Razas dispnibles:

┌───────┬─────────┬───────┐
│  1    │    2    │   3   │
├───────┼─────────┼───────┤
│opcion1│ opcion2 │opcion3│
└───────┴─────────┴───────┘

○ Listado de ventajas y desventajas de raza 1
○ Listado de ventajas y desventajas de raza 2
○ Listado de ventajas y desventajas de raza 3

Elige tu raza: RAZA

>El personaje no es muy resistente!
>El usuario ingresó X respuesta y fueron:

LISTADO DE RESPUESTAS

Resumen de personaje:
Nombre:
Edad:
Raza:
Fuerza:
Agilidad:
Destreza:
Defensa:
Magia:

'''