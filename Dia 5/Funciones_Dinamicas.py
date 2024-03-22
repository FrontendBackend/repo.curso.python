'''
Práctica Funciones Dinámicas 1
Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores
de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con
valores positivos y negativos.

No invoques la función, solo es necesario definirla.
'''
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero <= 0:
            return False
    return True

# Definir la lista de números
lista_numeros = [1, 2, 3, -4, 5, -6]




'''
Práctica Funciones Dinámicas 2
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y 
cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
'''
def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if 0 < numero < 1000:
            suma += numero
    return suma

# Definir la lista de números
lista_numeros = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]





'''
Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y 
devuelva el resultado de dicha cuenta.
'''
def cantidad_pares(lista_numeros):
    cantidad = 0
    for c in lista_numeros:
        if c %2==0:
            cantidad += 1
    return cantidad
lista_numeros = [2,4,6,7,8,9,10,11,12,16,18,20,25]
print(cantidad_pares(lista_numeros))



