# Práctica Zip 1
# Muestra en pantalla frases como la del siguiente ejemplo:

# La capital de Alemania es Berlín

# Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

x = list(zip(capitales,paises))

for capitales,paises in x:
    print(f"La capital de {paises} es {capitales}")






# Práctica Zip 2
# Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
# Listas de marcas y productos
marcas = ["Nike", "Adidas", "Apple", "Samsung", "Sony"]
productos = ["Zapatillas", "Camisetas", "iPhone", "Teléfonos", "TVs"]

# Crear un objeto zip
mi_zip = zip(marcas, productos)
print(mi_zip)






# Práctica Zip 3
# Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

# uno / um / one

# dos / dois / two

# tres / três / three

# cuatro / quatro / four

# cinco / cinco / five

# El resultado deberá seguir la estructura:

# [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]

# Crear un objeto zip con las traducciones
numeros_zip = zip(["uno", "dos", "tres", "cuatro", "cinco"],
                  ["um", "dois", "três", "quatro", "cinco"],
                  ["one", "two", "three", "four", "five"])

# Convertir el objeto zip en una lista
numeros = list(numeros_zip)

# Imprimir la lista resultante
print(numeros)








