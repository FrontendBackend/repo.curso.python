'''-----------------------------------------------------------------'''
'''---------------------------- HERENCIA ---------------------------'''
'''-----------------------------------------------------------------'''
'''
Práctica Herencia 1
Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad.
Crea otra clase, Alumno, que herede de la primera estos atributos.
'''
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass



'''
Práctica Herencia 2
Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: 
edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.
'''
class Mascota:

    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass



'''
Práctica Herencia 3
Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() 
(puedes dejar el código de los métodos en blanco con pass). 
Crea una clase llamada Automovil que herede estos métodos de Vehiculo.
'''
class Vehiculo:

    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass



'''-----------------------------------------------------------------'''
'''------------------------HERENCIA EXTENDIDA-----------------------'''
'''-----------------------------------------------------------------'''

'''
Práctica Herencia Extendida 1
Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, 
y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a 
esta clase heredar correctamente de Padre y Madre.

Completa el código suministrado a continuación para lograrlo.
'''
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class Hija(Madre, Padre):
    pass  # No necesitamos añadir más métodos en este caso


# Ejemplo de uso
hija = Hija()
hija.trabajar()  # Llamada al método trabajar heredado de Padre
hija.reir()  # Llamada al método reir heredado de Padre




'''
Práctica Herencia Extendida 2
"El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; y 
amamanta a sus crías pero no tienen mamas." (National Geographic)

Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, 
tal que "construyas" un animal que tiene los siguientes métodos y atributos:

- poner_huevos()

- tiene_pico = True

- vertebrado = True

- venenoso = True

- nadar()

- caminar()

- amamantar()
'''
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre
        self.venenoso = True  # El ornitorrinco es venenoso

    def poner_huevos(self):  # Sobrescribe el método poner_huevos
        print("Poniendo huevos")

    def nadar(self):  # Sobrescribe el método nadar de Pez
        print("Nadando")

    def caminar(self):  # Sobrescribe el método caminar de Mamifero
        print("Caminando")

    def amamantar(self):  # Sobrescribe el método amamantar de Mamifero
        print("Amamantando crías")



'''
Práctica Herencia Extendida 3
Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. 
Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método hobby() 
para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"

[1]: asegúrate de utilizar return seguido de una cadena de texto
'''


class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def __init__(self):
        super().__init__()

    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

'''--------------------Resultado alternativo-----------------'''


class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"


# Ejemplo de uso
padre = Padre()
hijo = Hijo()

print("Padre:")
print("Color de ojos:", padre.color_ojos)
print("Tipo de pelo:", padre.tipo_pelo)
print("Altura:", padre.altura)
print("Voz:", padre.voz)
print("Deporte preferido:", padre.deporte_preferido)
print("Risa:", padre.reir())
print("Hobby:", padre.hobby())
print("Caminar:", padre.caminar())

print("\nHijo:")
print("Color de ojos:", hijo.color_ojos)
print("Tipo de pelo:", hijo.tipo_pelo)
print("Altura:", hijo.altura)
print("Voz:", hijo.voz)
print("Deporte preferido:", hijo.deporte_preferido)
print("Risa:", hijo.reir())
print("Hobby:", hijo.hobby())
print("Caminar:", hijo.caminar())



