def mi_generador():

    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()

print(next(g))
print(next(g))
print('Hola mundo')
print(next(g))



'''
Práctica Generadores 1
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, 
iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.
'''
def generador_infinito():
    num = 1
    while True:
        yield num
        num += 1

# Crear el generador
generador = generador_infinito()

# Ejemplo de uso
print(next(generador))  # Devuelve 1
print(next(generador))  # Devuelve 2
print(next(generador))  # Devuelve 3
print(next(generador))  # Devuelve 3
print(next(generador))  # Devuelve 3
print(next(generador))  # Devuelve 3
print(next(generador))  # Devuelve 3
# Y así sucesivamente...




'''
Práctica Generadores 2
Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, 
iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).
'''

def generador_multiplos_de_7():
    num = 7
    while True:
        yield num
        num += 7

# Crear el generador
generador = generador_multiplos_de_7()

# Ejemplo de uso
for _ in range(10):
    print(next(generador))


'''
Práctica Generadores 3
Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea 
llamado:

1. "Te quedan 3 vidas"
2. "Te quedan 2 vidas"
3. "Te queda 1 vida"
4. "Game Over"

Almacena el generador en la variable perder_vida
'''

def perder_vida(vidas):
    while vidas > 0:
        if vidas == 1:
            yield f"Te quedan {vidas} vida"
        else:
            yield f"Te queda {vidas} vidas"
        vidas -= 1
    yield "Game Over"

# Crear el generador
generador = perder_vida(3)

# Ejemplo de uso
for _ in range(4):
    print(next(generador))


'''----------Resultado alternativo-----------'''


def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))