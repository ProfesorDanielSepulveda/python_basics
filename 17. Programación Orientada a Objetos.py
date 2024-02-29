#PROGRAMACION ORIENTADA A OBJETOS

#Es un modo de programación que nos permite diseñar objetos digitales que podemos utilizar, manipular o destruir.
#Al código que define a un objeto lo llamamos "CLASE"
#Permiten agrupar un conjunto de funciones y variables para nuestros objetos tengan vida.

#Por ejemplo:
#Al crear una clase para definir el concepto de "Ave", dentro de esta clase podría definir las caracteristicas (tipo, color, tamaño, etc) estos son atributos del objeto
#Las clases tienen un conjunto de funcionalidades que pueden hacer, mi pájaro puede piar, comer, volar, etc, que serán sus métodos.
#Luego, puedo tener muchos pájaros: gorrión, halcón o incluso de otros nombres. Cada uno de ellos será un objeto particular.
#Entonces, mi clase sería pájaro, pero halcón o cuervo son objetos, instancias de una clase específica.

#La programación orientada a objetos está basada en 6 pilares básicos:
# Herencia
# Polimorfismo
# Cohesion
# Abstracción
# Acoplamiento
# Encapsulamiento

#Para poder comprender de manera sencilla el concepto de clase y objeto, vamos a realizar ejemplos con un gato.
#Crearemos la clase 'gato' (ojo a la mayúscula, que por convención se tipea así):
#Esta clase está vacía:

class Gato:
  pass

#Ahora puedo utilizar la clase para crear un par de objetos basados en la clase:

silvestre = Gato()
michi = Gato()

print(type(silvestre))
<class '__main__.Gato'>
print(type(michi))
<class '__main__.Gato'>

#Como puedes apreciar, estas variables no son el típico dato que hemos visto anteriormente
#No son int, no son str, no son listas. Son "silvestre" y "michi", cada uno de ellos es una instancia de la clase "Gato"
#Si llamamos a los objetos directamente, nos muestra los objetos individuales:

print(silvestre)
<__main__.Gato object at 0x000002237518FA50>
print(michi)
<__main__.Gato object at 0x000002237579CC50>

#Pero nuestra clase está vacía. Estos Gatos no saben hacer nada y no tienen ninguna característica particular.
#Vamos a darles atributos

#Hay dos clases de atributos: de clase y de instancia

#Los atributos de clase son comunes a todos los objetos de esa clase específica
#Los atributos de instancia son específicos de cada una de las instancias de la clase
#Ejemplo: Gato tiene un atributo de clase que podría ser "cola", todos los gatos tienen una sola cola.
#Pero puedo tener un atributo de instancia que puede ser color, el color será distinto para cada gato.

#Vamos a crear los atributos de instancia color y peso
#también crearemos los atributos de clase cola y patas:

#Creo la clase
class Gato:

  cola = True
  patas = 4

  def __init__(self, color, peso):
    self.color = color
    self.peso = peso


#Vamos a definir la estructura de lo que acabamos de crear.
#Gato es el nombre de la clase.
#Nuestros atributos de clase: cola y patas, se declaran directamente dentro de la clase
#Una vez declarado, cada instancia del objeto que se cree tendrá los atributos de clase
#El método def __init__ permite que se ejecute una secuencia AL CREAR UN OBJETO
#Los parametros que siguen son las instrucciones que se ejecutarán en la secuencia de inicio.
#self es una palabra de autoreferencia, indica que debe pedirse algo para ser asignado.
#Luego se deben llamar en orden los atributos y los parámetros.
#IMPORTANTE: Podríamos utilizar nombres distintos para atributos y parámetros y funcionaría exactamente igual, pero por convención se utilizan los mismos


#En este caso, hemos creado la clase gato, que posee dos atributos de clase: cola y patas
#y que posee dos atributos de instancia: color y peso

#Luego, cuando creemos nuevamente los objetos, debemos hacerlo entregando los atributos de instancia EN EL ORDEN CREADO
#Si no lo hacemos, nos arrojará un error:

silvestre = Gato()
Traceback (most recent call last):
  File "C:\Users\dasep\OneDrive\Desktop\asd.py", line 10, in <module>
    silvestre = Gato()
TypeError: Gato.__init__() missing 2 required positional arguments: 'color' and 'peso'

#Creemos dos gatos:
silvestre = Gato('Negro', 85)
michi = Gato('Blanco', 65)

#Luego, con mis objetos creados, puedo invocar sus atributos como haría con cualquier otro atributo:
print(silvestre.cola)
True
print(silvestre.patas)
4
print(silvestre.color)
Negro
print(silvestre.peso)
85

print(michi.cola)
True
print(michi.patas)
4
print(michi.color)
Blanco
print(michi.peso)
65

#Tal como mencionamos anteriormente, los atributos de clase son comunes a todos los objetos de la clase
#mientras que los atributos de instancia son particulares de cada objeto.


######EJERCICIO######
#Crea una clase llamada 'Cuenta_Bancaria'
#La clase debe tener los atributos de instancia: número de cuenta, tipo de cuenta
#La clase debe tener el atributo de instancia saldo, que debe ser igual a 0

#Crea dos objetos a partir del formato cta(rutusuario) con los siguientes datos:
# Nro Cta: 1563-569-8564 Tipo Cta: Corriente.
# Nro Cta: 254698-856921 Tipo Cta: Vista.

#Luego llama a los objetos mostrando sus atributos


###SOLUCION###

class Cuenta_Bancaria:
  saldo = 0

  def __init__ (self, nro_cta, tipo_cta):
    self.nro_cta = nro_cta
    self.tipo_cta = tipo_cta

cta12345678 = Cuenta_Bancaria("1563-569-8564", "Corriente")
cta87654321 = Cuenta_Bancaria("254698-856921", "Vista")

print(f"La cuenta del cliente 12345678 tiene nro: {cta12345678.nro_cta}, es de tipo {cta12345678.tipo_cta} y tiene saldo: ${cta12345678.saldo}")
La cuenta del cliente 12345678 tiene nro: 1563-569-8564, es de tipo Corriente y tiene saldo: $0

print(f"La cuenta del cliente 87654321 tiene nro: {cta87654321.nro_cta}, es de tipo {cta87654321.tipo_cta} y tiene saldo: ${cta87654321.saldo}")
La cuenta del cliente 87654321 tiene nro: 254698-856921, es de tipo Vista y tiene saldo: $0





###MÉTODOS###

###DE INSTANCIA

#Ahora que ya hemos visto lo básico sobre programación orientada a objetos,
#nos moveremos a crear métodos de instancia y seguiremos trabajando con la clase cuenta bancaria creada en el ejercicio anterior

class Cuenta_Bancaria:
    saldo = 0

    def __init__ (self, nro_cta, tipo_cta):
        self.nro_cta = nro_cta
        self.tipo_cta = tipo_cta

    #Crear un método es muy similar a crear una función, solo que hay algunos detalles:
    #El método debe estar inserto en el interior de la clase
    #Los métodos SIEMPRE deben tener un valor por defecto
    #Ese valor es self
                   ↓
    def depositar(self, monto):
        print(f"Depositando {monto}")
        self.saldo = self.saldo + monto
                         ↑
        #Tal como se ve aqui,
        #Siempre que en un método hagamos referencia a un atributo de la clase, debemos usar el prefijo self.
        #Si el método necesita argumentos, esos argumentos se pueden ingresar tras el self,
        #En este caso, este metodo recibe un argumento: monto

    #En este caso, este método no recibe argumentos.
    def resetear(self):
        self.saldo = 0


cta12345678 = Cuenta_Bancaria("1563-569-8564", "Corriente")
cta87654321 = Cuenta_Bancaria("254698-856921", "Vista")

#Para llamar el método, simplemente lo invocamos pasandole el argumento que necesita para funcionar
cta12345678.depositar(500000)
Depositando 500000
cta87654321.depositar(20000)
Depositando 20000


print(f"La cuenta del cliente 12345678 tiene nro: {cta12345678.nro_cta}, es de tipo {cta12345678.tipo_cta} y tiene saldo: ${cta12345678.saldo}")
La cuenta del cliente 12345678 tiene nro: 1563-569-8564, es de tipo Corriente y tiene saldo: $500000
print(f"La cuenta del cliente 87654321 tiene nro: {cta87654321.nro_cta}, es de tipo {cta87654321.tipo_cta} y tiene saldo: ${cta87654321.saldo}")
La cuenta del cliente 87654321 tiene nro: 254698-856921, es de tipo Vista y tiene saldo: $20000

#Si el método no necesita argumentos, entonces no se le pasa ninguno
cta12345678.resetear()
cta87654321.resetear()

print(f"La cuenta del cliente 12345678 tiene nro: {cta12345678.nro_cta}, es de tipo {cta12345678.tipo_cta} y tiene saldo: ${cta12345678.saldo}")
La cuenta del cliente 12345678 tiene nro: 1563-569-8564, es de tipo Corriente y tiene saldo: $0
print(f"La cuenta del cliente 87654321 tiene nro: {cta87654321.nro_cta}, es de tipo {cta87654321.tipo_cta} y tiene saldo: ${cta87654321.saldo}")
La cuenta del cliente 87654321 tiene nro: 254698-856921, es de tipo Vista y tiene saldo: $0


###DE CLASE
#Los métodos clase permiten poder realizar métodos que no afectan a las instancias particulares, sino a la clase completa en si.
#Para poder utilizar un método de clase, lo catalogamos con el decorador @classmethod
#En los métodos de clase, en lugar de self utilizamos cls.

###ESTÁTICOS
#Los métodos estáticos permiten poder realizar métodos que no afectan a las instancias particulares ni a las clases, sino solo generan una secuencia aislada.
#Para poder utilizar un método estático, lo catalogamos con el decorador @staticmethod
#En los métodos estáticos, no utilizamos catalogadores:

class Cuenta_Bancaria:
    saldo = 0

    def __init__(self,nro_cta,tipo_cta):
        self.nro_cta = nro_cta
        self.tipo_cta = tipo_cta

    def depositar(self, monto):
        self.saldo += monto
        print("Monto depositado")

    def resetear(self):
        self.saldo = 0

    #METODO DE CLASE
    @classmethod
    def v_prev(cls, nuevo_monto):
        cls.saldo = int(nuevo_monto)
        print(f"A partir de ahora todas las nuevas cuentas tendrán saldo {cls.saldo}")

    #METODO ESTATICO
    @staticmethod
    def help():
        print("Métodos:\ndepositar: deposita un monto.\nresetear: resetea saldo a $0.\nv_prev: cambia monto inicial")



Cuenta_Bancaria.v_prev(50000)
A partir de ahora todas las nuevas cuentas tendrán saldo 50000

cta1718 = Cuenta_Bancaria(1415, "Corriente")

print(cta1718.saldo)
50000

Cuenta_Bancaria.help()
Métodos:
depositar: deposita un monto.
resetear: resetea saldo a $0.
v_prev: cambia monto inicial



###HERENCIA###

#La herencia es uno de los pilares de la programación orientada a objetos.
#A través de la herencia un objeto puede heredar de otro atributos y métodos
#De esta manera, una clase 'madre' puede pasarle a otra clase 'hija' sus características.
#Para poder generar la herencia, debe declararse la clase en el formato:
#class hija(Madre):

#Para poder comenzar a explorar la herencia, lo primero que haremos será generar clases vacías que hereden de una madre.
#Para eso, generaremos la clase Cuenta y las subclases Corrienta y Vista:

class Cuenta:
    pass

class Corriente(Cuenta):
    pass

class Vista(Cuenta):
    pass

#podemos explorar quien es la madre de la clase Corriente y Vista:
print(Corriente.__bases__)
(<class '__main__.Cuenta'>,)

print(Vista.__bases__)
(<class '__main__.Cuenta'>,)

#También podemos ver cuales son las subclases de Cuenta:
print(Cuenta.__subclasses__())
[<class '__main__.Corriente'>, <class '__main__.Vista'>]


#Entonces
#Vamos a practicar heredando de cuenta varios de nuestros métodos:
#Tal como pueden apreciar aquí, las clases Vista y Corriente heredan todas las características que hay en Cuenta
#Además, cada una de ellas tiene un atributo propio llamado tipo, que es diferente en cada una de ellas.

class Cuenta:
    saldo = 0

    def __init__(self,nro_cta):
        self.nro_cta = nro_cta

    def depositar(self, monto):
        self.saldo += monto
        print("Monto depositado")

    def resetear(self):
        self.saldo = 0

    @classmethod
    def v_prev(cls, nuevo_monto):
        cls.saldo = int(nuevo_monto)
        print(f"A partir de ahora todas las nuevas cuentas tendrán saldo {cls.saldo}")

    @staticmethod
    def help():
        print("Métodos:\ndepositar: deposita un monto.\nresetear: resetea saldo a $0.\nv_prev: cambia monto inicial")


class Corriente(Cuenta):
    tipo = "Corriente"

class Vista(Cuenta):
    tipo = "Vista"


cta12345678 = Corriente(12345678)
cta87654321 = Vista(87654321)

print(cta12345678.tipo)
Corriente
cta12345678.depositar(75000)
Monto depositado
print(cta12345678.saldo)
75000

print(cta87654321.tipo)
Vista
cta87654321.depositar(50000)
Monto depositado
print(cta87654321.saldo)
50000



#Una clase puede heredar de varias clases al mismo tiempo: NombreClase(padre, madre)
#Tambien, una clase puede haber heredado un método de alguno de sus padres y sobreescribirlo.
#Si una clase hereda de su madre el método x y luego hereda este mismo método a otra clase, entonces el método modificado es el que se hereda.
#Ejemplo:

class Clase1:
    @staticmethod
    def metodo():
        print("Este es el método original")

class Clase2(Clase1):
    @staticmethod
    def metodo():
        print("Este es el método modificado")

class Clase3(Clase2):
    pass


Clase3.metodo()



###POLIMORFISMO###

#El polimorfismo es una caracteristica que dice que distintas clases y, por tanto, distintos objetos,
#pueden compartir métodos de igual nombre:

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice miau")


class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice guau")

michi = Gato("michi")
cachupin = Perro("cachupin")

michi.hablar()
michi dice miau

cachupin.hablar()
cachupin dice guau


#Si los métodos se llaman igual, entonces podríamos iterarlos:
lista = [michi, cachupin]

for objeto in lista:
    objeto.hablar()

michi dice miau
cachupin dice guau

#SI podemos iterarlos, podemos administrarlos en funciones:

def hablar(animal):
    animal.hablar()

hablar(michi)
hablar(cachupin)

michi dice miau
cachupin dice guau



###COHESION###

#La cohesión se refiere al grado de relación entre los elementos de un módulo.
#Cuando diseñamos una función, debemos identificar de un modo bien específico qué tarea va a realizar,
#reduciendo su finalidad a un objetivo único y bien definido.

#En resumen: para que una función sea cohesiva debe hacer solo una cosa,
#y si tiene que hacer más de una cosa, estas deben tener una alta relación entre sí.
#Cuantas más cosas haga una función sin relación entre sí, más complicado será entender el código.

#Existen dos tipos de cohesión:

#Cohesión débil: indica que la relación entre los elementos es baja, y por lo tanto no tienen una única funcionalidad.
#Cohesión fuerte: indica que existe una alta relación entre los elementos existentes dentro del módulo. Este debe ser nuestro objetivo al diseñar programas.
#Un ejemplo bien claro de cohesión débil o fuerte podría ser el siguiente:

#Queremos tener una función llamada suma() cuya finalidad sea sumar dos argumentos numéricos.
#Una versión con cohesión fuerte de esta función sería la siguiente:

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

#El problema ocurriría si al programador le dan ganas de poner todo en un solo sitio, y además de sumar dos números, aprovecha esta función para:
#pedirle al usuario que ingrese esos números (en vez de pedirlo en otra función y pasarlos como argumentos),
#y como va a necesitar que esos numeros sean float() también va a hacer la conversión dentro de la misma función.
#El resultado de añadir estas funcionalidades sería una función de cohesión débil:

def suma():
    num1 = float(input("Elige un número"))
    num2 = float(input("Elige otro número"))
    resultado = num1 + num2
    return resultado

#Podrías estar pensando que estas otras dos funcionalidades extra no son para tanto,
#pero supongamos que una persona quiere usar nuestra función suma()
#pero ya tiene los números y no quiere pedirlos por pantalla, nuestra función no le serviría.

#Para que la función tuviese una cohesión fuerte, sería conveniente que suma() realizara una única tarea bien definida, que es sumar.



###ACOPLAMIENTO###

#El acoplamiento es un concepto que mide la dependencia entre dos módulos distintos (como por ejemplo, clases). Podemos hablar de dos tipos:

#Acoplamiento débil, que implica que no hay dependencia entre un módulo y otros. Esta es la situación ideal.
#Acoplamiento fuerte, que es la situación contraria, e indica que el módulo tiene dependencias internas con otros.
#Se trata de un pilar vinculado con la cohesión, ya que por lo general un acoplamiento débil se asocia a una cohesión fuerte.
#Esta última es la situación buscada al escribir código.
#Es decir, buscamos que una clase o función no tenga dependencias con otras clases o funciones, y que las tareas que realizan estén relacionadas entre sí.
#Esto simplifica la lectura y mantenimiento del código , a la vez que permite reutilizarlo en otros programas.

#Para terminar de comprenderlo, imaginemos la situación contraria: un código fuertemente acoplado:

#Si quisiéramos reutilizar un módulo que depende de otros, deberíamos “traer” también todas las dependencias,
#de lo contrario resultaría en errores y pérdida de funcionalidad.
#Si efectuamos un cambio en un módulo dependiente de otros, los efectos de este cambio pueden afectar a los otros módulos que dependen del anterior.
#Es muy importante prestarle atención a medida que nuestros programas crecen y se hacen más complejos,
#donde este tipo de situaciones pueden comenzar a ocurrir inadvertidamente.
#Si esto sucede, un cambio en una clase puede inutilizar otra, haciendo que deje de funcionar.
#Una situación de acoplamiento fuerte puede originar errores que son difíciles de depurar.

#Veamos el siguiente ejemplo:

class Mascota:
    tiene_patas = True
    pass

class Perro:
    def correr(self, velocidad):
        if Mascota.tiene_patas:
            self.velocidad = velocidad

mi_mascota = Perro()
mi_mascota.correr("rápido")
print(mi_mascota.velocidad)

#Tenemos una clase Mascota que define un atributo de clase tiene_patas.
#Por otra parte, la clase Perro basa el comportamiento del método correr() en el atributo tiene_patas de la clase Mascota.
#Tenemos acoplamiento fuerte, ya que hay una dependencia entre la función de una clase con el atributo de otra.

#Si tu programa debe contener dependencias externas,
#deberás asegurarte que las mismas son esenciales y están debidamente justificadas para minimizar los efectos adversos mencionados.



###ABSTRACCION###

#La abstracción es el pilar de la programación orientada a objetos que se relaciona con ocultar toda la complejidad que algo puede tener por dentro,
#ofreciendo una interfaz con funciones de alto nivel, por lo general sencillas de usar,
#que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que hay dentro.

#Piensa en cuántos objetos de ingeniería o aplicaciones utilizas en tu día a día,
#que tienen una interfaz sencilla y por dentro un comportamiento complejo.

#¿Qué sucedería si para poder conducir debiéramos conocer cada uno de los detalles de funcionamiento de un automóvil,
#desde el giro de sus engranajes al circuito eléctrico que alimenta el mecanismo que sube y baja los vidrios de las ventanillas?
#Para operar este último, un conducto solamente necesita accionar un botón y que el mismo realice la acción esperada.
#Este botón abstrae al conductor de un sistema complejo y le proporciona una interfaz sencilla para lograr su objetivo.
#Si lo programáramos, los métodos podrían ser subir() y bajar(), y en su interior, distribuir energía y accionar mecanismos en los diferentes sectores del vehículo.

#A esto mismo debe apuntar nuestro código: sin importar lo complejo que necesite ser en su interior,
#una buena abstracción permite ofrecer métodos sencillos y de funcionamiento predecible de acuerdo con su denominación.



###ENCAPSULAMIENTO###
#El encapsulamiento es el pilar de la programación orientada a objetos que se relaciona con ocultar al exterior determinados estados internos de un objeto,
#tal que sea el mismo objeto quien acceda o los modifique, pero que dicha acción no se pueda llevar a cabo desde el exterior,
#llamando a los métodos o atributos directamente.

#Si bien en algunos lenguajes (como Java), puede resultar un procedimiento habitual,
#Python no lo implementa por defecto, pero nos propone una vía alternativa para lograrlo.
#Esto se hace anteponiendo dos guiones bajos (__) al nombrar un método o atributo.
#De esa manera, los mismos quedarán definidos como “privados”, y únicamente el mismo objeto podrá acceder a ellos.

class Persona:
    atributo_publico = "Mostrar"   # Accesible desde el exterior
    __atributo_privado = "Oculto"  # No accesible
    # No accesible desde el exterior
    def __metodo_oculto(self):
        print("Este método está oculto")
        self.__variable = 0
    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__metodo_oculto()

alumno = Persona()
# alumno.__metodo_oculto()  # Este método no es accesible desde el exterior
alumno.metodo_normal()      # Este método es accesible

#Existe un pequeño truco (no recomendado) para acceder a los atributos y métodos ocultos.
#Dichos métodos están presentes con un nombre algo distinto:
#instancia + _ + NombreClase + método/atributo oculto

alumno._Persona__metodo_oculto()
print(alumno._Persona__atributo_privado)