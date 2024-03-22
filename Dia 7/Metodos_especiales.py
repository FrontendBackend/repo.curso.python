'''
Práctica Métodos Especiales 1
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto,
devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).
'''


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

# Ejemplo de uso:
libro = Libro("El principito", "Antoine de Saint-Exupéry", 4)
print(libro)  # Salida: "El principito", de Antoine de Saint-Exupéry



'''
Práctica Métodos Especiales 2
Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute 
la función len() sobre el mismo, devuelva el número de páginas como número entero.
'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas

libro = Libro("El principito", "Antoine de Saint-Exupéry", 4)
print(len(libro))  # Salida: "El principito", de Antoine de Saint-Exupéry



'''
Práctica Métodos Especiales 3
Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con 
el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine.
'''

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        return print("Libro eliminado")

libro = Libro("El principito", "Antoine de Saint-Exupéry", 4)
del libro



