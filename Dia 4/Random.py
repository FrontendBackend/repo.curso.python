# Práctica Random 1
# Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio
from random import randint

# Utiliza randint para generar un número aleatorio entre 1 y 10
aleatorio = randint(1, 10)

print("Número aleatorio generado:", aleatorio)





# Práctica Random 2
# Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio
from random import *

# Utiliza random para generar un número decimal entre 0 y 1
aleatorio = random()

print("Número aleatorio generado:", aleatorio)




# Práctica Random 3
# Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
from random import choice

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

# Utiliza choice para seleccionar un nombre al azar de la lista
sorteo = choice(nombres)

print("Nombre seleccionado en el sorteo:", sorteo)