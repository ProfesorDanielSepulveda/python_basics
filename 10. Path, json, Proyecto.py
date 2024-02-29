"""Path y json
"""

#Path nos permite poder manipular archivos y rutas.
#Debe importarse desde la librería pathlib

from pathlib import Path
import json

#Lo mejor es siempre declarar una ruta base.
#Puede hacerse de muchas formas:

#A través del home
ruta_base = Path(Path.home())

#Construida manual:
ruta_base = Path('C:/users/usuario/desktop')

#Rutas relativas:
ruta_base = Path('archivo.py').resolve().parent

#Crea un directorio:
Path("NOMBRE DIRECTORIO").mkdir()

#Borra un directorio: (debe estar vacío)
Path("NOMBRE DIRECTORIO").rmdir()

#Crea un archivo nuevo:
Path("NOMBRE ARCHIVO.EXTENSION").touch()

#Borra un archivo:
Path("NOMBRE ARCHIVO.EXTENSION").unlink()

#podemos iterar el contenido de un directorio para mostrarlo a traves de un loop for
#iterdir() itera sobre TODO el contenido.
Path(ruta_base).iterdir()

#ejemplo:

for elemento in Path(ruta_base).iterdir():
    print(elemento)

#Para poder buscar tipos de archivos o patrones, se puede usar glob()
Path(ruta_base).glob()

#Patrones:
# "*.EXTENSION" -> Todos los que haya en el directorio buscado
# "**/*.EXTENSION" -> Todos los que haya en directorio y subdirectorios

#ejemplo (imprime todos los pdf):
for archivo in Path(ruta_base).glob('*.pdf'):
    print(archivo)

#Para construir rutas, debemos agregarlas directamente al objeto Path:
#podemos hacerlo con , o con /

ruta = Path(ruta_base, "CARPETA_1", "CARPETA_2", "CARPETA_3", "archivo.txt")
ruta = Path(ruta_base/"CARPETA_1"/"CARPETA_2"/"CARPETA_3"/"archivo.txt")



#ARCHIVOS TXT

ARCHIVO = Path(ruta_base/'carpeta'/'archivo.txt')

#Ver contenido de un archivo
#Arrojado dentro de un print, muestra el contenido de un archivo:
Path(ARCHIVO).read_text()

#Escribir informacion en un archivo
#Permite ingresar contenido a un archivo, para generar nuevas lineas sin
#borrar las anteriores, se debe llamar el contenido previo con un read y concatenar
Path(ARCHIVO).write_text("Texto a insertar")
Path(ARCHIVO).write_text(ARCHIVO.read_text() + "\nTexto a insertar")



#ARCHIVOS JSON

#Un archivo json maneja infomración de datos en clave, valor, como un diccionario.

#Crear un archivo JSON
Path(ruta/'archivo.json').touch()

#Eliminar un archivo JSON
Path(ruta/'archivo.json').unlink()

#Para insertar datos dentro de un archivo json, primero debemos tener los datos:
datos = [{'ID': 1001 ,'nombre': 'Carlos', 'Edad': 40, 'direccion': 'calle123'}]

#Es posible cargar datos a un archivo de json usando el método dump:
json.dump(datos, archivo)
#Pero cargar datos a un archivo json requiere que se lea el archivo primero en modo escritura:
#esto se hace con open(archivo, 'w')
#por tanto:
json.dump(datos, open(archivo, 'w'))

#Esto puede reducirse usando el comando with:

with open(archivo, 'w') as archivo:
    json.dump(datos, archivo)


#Ahora podemos leer la información del archivo usando el método load
#la función de open ahora debe ser r en lugar de w

with open(archivo, 'r') as archivo:
    datos = json.load(archivo)
    print(datos)

#> [{'ID': 1001 , 'nombre': 'Carlos', 'Edad': 40, 'direccion': 'calle123'}]


#Para agregar nuevos datos al archivo, primero debemos leer el contenido
#Luego debemos cargar los datos nuevos a modo de diccionario y agregarlos a la lista
#Luego, debemos cargar la lista actualizada hacia el archivo nuevamente

id = 1002
name = 'carla'
edad = 20
direccion = 'calle 321'
datos = {'ID': id, 'nombre': name, 'edad': edad, 'direccion': direccion}

with open(archivo, 'r') as archivo:
    personas = json.load(archivo)

personas.append(datos)

with open(archivo, 'w') as archivo:
    personas = json.dump(datos, archivo)



#¿Cómo buscar datos en esta base de datos?

#Primero, necesitamos un elemento único que no se repita e identifique a cada persona
#El mejor candidato es el ID
#Luego, recorreremos la base de datos, buscando a cada persona
#Por cada persona, verificaremos el ID y si el el ID corresponde
#Entonces podemos llamar los datos.

id_buscado = 1002

with open(archivo, 'r') as archivo:
    personas = json.load(archivo)

for persona in personas:
    if persona['ID'] == id_buscado:
        print(f"'ID': {persona['ID']}, 'nombre': {persona['nombre']}, 'edad': {persona['edad']}, 'direccion': {persona['direccion']}")
    break
  
"""
'ID': 1002
'nombre': carla
'edad': 20
'direccion': calle 321
"""

#¿Cómo editar los datos de una persona?
#Primero, tenemos que encontrar a la persona.
#Una vez encontrada, debemos editar los datos
#Una vez editados los datos, debemos cargar la información hacia el archivo

id_buscado = 1002
nuevo_nombre = 'Josefa'
persona_encontrada = False

with open(archivo, 'r') as archivo:
    personas = json.load(archivo)

for persona in personas:
    if persona['ID'] == id_buscado:
        persona_encontrada = True
        persona['nombre'] = nuevo_nombre
        break

if persona_encontrada:
    with open(archivo, 'w') as archivo:
        json.dump(personas, archivo)
        print('Los datos fueron editados correctamente')

if not persona_encontrada:
    print(f'No se encontró el ID {id_buscado} en la base de datos')



#EJERCICIO PROYECTO
'''
Vamos a generar un programa.
El objetivo del programa es manejar las hojas de vida de los trabajadores de una empresa.
El sistema se compone de: hojas de vida, hoja de anotaciones.

La ficha de cada trabajador debe tener los siguientes campos:
Nombre: En formato str
Fecha de nacimiento: en formato 00/00/0000
Codigo de empleado: en formato 0000
Telefono: en formato (+569)12345678
Correo: en formato correo@correo.cl
Direccion: en formato calle #número - comuna

La hoja de anotaciones debe contener los siguientes campos POR CADA ANOTACION:

Código: rut-0000 (formato numerico ascendente)
Fecha: en formato 00/00/0000
Detalle: Descripción de la anotación

El sistema debe ofrecer varios menus:

1. Empleados
  1.1. Registrar nuevo empleado (desencadena proceso de crear una nueva ficha y generar una nueva hoja de anotaciones)
  1.2. Editar datos de empleado (Permite editar datos de la ficha del trabajador)
  1.3. Volver (regresa al menu principal)

2. Anotaciones
  2.1. Ingresar anotación (Ingresa una nueva anotación)
  2.2. Editar anotación
    2.2.1 Seleccionar trabajador (mostrar una lista de los trabajadores y permitir seleccionar uno)
      2.2.1.1 Seleccionar anotación (mostrar listado de las anotaciones del trabajador seleccionado y permitir seleccionar una para editarla)
        2.2.1.1.1 Permitir seleccionar el campo especifico a editar y editarlo
  2.3. Eliminar anotación
    2.3.1 Seleccionar trabajador (mostrar una lista de los trabajadores y permitir seleccionar uno)
      2.3.1.1 Seleccionar anotación (mostrar listado de las anotaciones del trabajador seleccionado y eliminarla)
  2.4 Volver (regresa al menu principal)

3. Reportes
  3.1 Reporte de códigos (mostrar una lista de todos los empleados y sus códigos de empleados.)
  3.2 Reporte de medios de contacto (mostrar una lista de todos empleados y sus teléfonos y correos.)
  3.3 Reporte de anotaciones
    3.3.1 Seleccionar trabajador (mostrar una lista de los trabajadores y permitir seleccionar uno, lo que mostrará todas las anotaciones vinculadas a él)
  3.4 Volver (regresa al menu principal)

4. Salir (cierra el programa)


'''