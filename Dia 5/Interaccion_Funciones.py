'''
Práctica sobre Interacción entre Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función
debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
'''
import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Llamar a la función lanzar_dados y pasar los resultados a la función evaluar_jugada
resultado_dado1, resultado_dado2 = lanzar_dados()
print(evaluar_jugada(resultado_dado1, resultado_dado2))






'''
Práctica sobre Interacción entre Funciones 2
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y 
devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el 
valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que 
calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
'''

def reducir_lista(lista):
    # Eliminar duplicados y ordenar la lista
    lista_sin_duplicados = sorted(set(lista))
    # Eliminar el valor más alto si la lista tiene más de un elemento
    if len(lista_sin_duplicados) > 1:
        lista_sin_duplicados.pop()
        print("resultado pue: ", lista_sin_duplicados)
    return lista_sin_duplicados

def promedio(lista):
    # Calcular el promedio de los valores en la lista
    if not lista:
        return 0  # Devolver 0 si la lista está vacía
    return sum(lista) / len(lista)

# Definir la lista de números
lista_numeros = [1, 2, 15, 7, 2]

# Llamar a la función reducir_lista y pasar el resultado a la función promedio
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)

print(resultado_promedio)






'''
Práctica sobre Interacción entre Funciones 3
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe 
poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del 
lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores 
y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla 
(devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
'''
import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado

def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif resultado_moneda == "Cruz":
        print("La lista fue salvada")
        return lista_numeros

# Definir la lista de números
lista_numeros = [1, 2, 3, 4, 5]

# Llamar a la función lanzar_moneda
resultado_moneda = lanzar_moneda()

# Llamar a la función probar_suerte y pasar el resultado del lanzamiento de la moneda y la lista de números
nueva_lista = probar_suerte(resultado_moneda, lista_numeros)

print(nueva_lista)







