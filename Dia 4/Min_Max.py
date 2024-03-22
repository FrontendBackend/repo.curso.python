# Práctica Min y Max 1
# Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)
print(valor_maximo)






# Práctica Min y Max 2
# Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]


rango = max(lista_numeros) - min(lista_numeros)
print(rango)

# ---------------------------------- resultado opcional --------------------------------
# Calcula el valor máximo y el valor mínimo en la lista
maximo = max(lista_numeros)
minimo = min(lista_numeros)

# Calcula la diferencia entre el valor máximo y el valor mínimo
rango = maximo - minimo

print("El rango entre el valor máximo y el mínimo es:", rango)
# -----------------------------------------------------------------------------------------------





# Práctica Min y Max 3
# Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

# diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

# Almacena dicho valor en una variable llamada edad_minima.

# También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2, "Darío":49}

# Obtener el mínimo valor de edades
edad_minima = min(diccionario_edades.values())

# Obtener el nombre que se ubica último en orden alfabético
ultimo_nombre = max(diccionario_edades.keys())

print("La edad mínima es:", edad_minima)
print("El último nombre en orden alfabético es:", ultimo_nombre)


