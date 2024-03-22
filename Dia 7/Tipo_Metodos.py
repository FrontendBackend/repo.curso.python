'''
Práctica Tipos de Métodos 1
Crea un método estático respirar() para la clase Mascota. Cuando se llame,
debe imprimir en pantalla "Inhalar... Exhalar"
'''

class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


Mascota.respirar()





'''
Práctica Tipos de Métodos 2
Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, 
estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.
'''
class Jugador:

    vivo = False # Valor predeterminado del atributo vivo

    @classmethod
    def revivir(cls):
        cls.vivo = True

# Ejemplo de uso
print(Jugador.vivo)  # Imprime False
Jugador.revivir()    # Llama al método de clase revivir()
print(Jugador.vivo)  # Imprime True



'''
Práctica Tipos de Métodos 3
Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de 
Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
'''
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

# Ejemplo de uso
arquero = Personaje(10)  # Creamos un Personaje con 10 flechas
print("Cantidad de flechas antes de lanzar:", arquero.cantidad_flechas)  # Imprime 10
arquero.lanzar_flecha()  # Llamamos al método lanzar_flecha
print("Cantidad de flechas después de lanzar:", arquero.cantidad_flechas)  # Imprime 9





