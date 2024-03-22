from collections import namedtuple
from collections import Counter

Persona = namedtuple('persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel)


'''
Práctica Módulo Collections 1
Aplica un Counter (contador) sobre la lista de números entregada a continuación, 
y almacénalo en una variable llamada contador
'''
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)


'''
Práctica Módulo Collections 2
Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, 
se cargue con el string "Valor no hallado".

Carga el diccionario, al menos, con el siguiente par de datos:

palabra clave = edad

valor = 44

Utiliza el método defaultdict del módulo Collections.
'''

from collections import defaultdict

# Crear un defaultdict con un valor predeterminado de "Valor no hallado"
mi_diccionario = defaultdict(lambda: "Valor no hallado")

# Agregar el par de datos al diccionario
mi_diccionario["edad"] = 44

# Acceder a una clave que no existe
print(mi_diccionario["nombre"])  # Devolverá "Valor no hallado"


'''
Práctica Módulo Collections 3
Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que permite 
insertar y eliminar elementos por ambos extremos.

Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa una deque a partir del 
módulo collections. Los elementos iniciales de la lista se brindan a continuación.

["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.
'''
from collections import deque

# Elementos iniciales de la lista
elementos_iniciales = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

# Crear una deque con los elementos iniciales
lista_ciudades = deque(elementos_iniciales)

# Agregar un elemento por la izquierda ---Linea de código añadido de manera opcional
lista_ciudades.appendleft("Tokio")

# Imprimir la lista de ciudades
print(lista_ciudades)

