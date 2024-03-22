# Práctica Comprensión de Listas 1
# Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

# Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [valor**2 for valor in valores]

print(valores_cuadrado)







# Práctica Comprensión de Listas 2
# Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

# Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]

# Utiliza comprensión de listas con una condición para seleccionar los valores pares
valores_pares = [valor for valor in valores if valor % 2 == 0]

print("Valores originales:", valores)
print("Valores pares:", valores_pares)






# Práctica Comprensión de Listas 3
# Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

# Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:

# °C = (°F - 32) * (5/9)

# o expresado de otro modo:

# (grados_fahrenheit-32)*(5/9)

# La lista de temperaturas es la siguiente:

# temperatura_fahrenheit = [32, 212, 275]
# Almacena esta nueva lista en una variable llamada grados_celsius
temperatura_fahrenheit = [32, 212, 275]

# Utiliza comprensión de listas para convertir los valores de Fahrenheit a Celsius
grados_celsius = [(fahrenheit - 32) * (5/9) for fahrenheit in temperatura_fahrenheit]

print("Temperaturas en grados Fahrenheit:", temperatura_fahrenheit)
print("Temperaturas en grados Celsius:", grados_celsius)