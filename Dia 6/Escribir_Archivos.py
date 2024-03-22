'''
Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
'''
# Cambiando el contenido del archivo
archivo = open('mi_archivo.txt', 'w')
archivo.write("Nuevo texto")
archivo.close()

# Abriendo el archivo en modo lectura y mostrando su contenido
leer = open('mi_archivo.txt', 'r')
contenido = leer.read()
print(contenido)
leer.close()



'''
Práctica Crear y Escribir Archivos 2
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
'''
# Añadiendo una línea al final del archivo
archivo = open('mi_archivo.txt', 'a')
archivo.write("\nNuevo inicio de sesión")
archivo.close()

# Abriendo el archivo en modo lectura y mostrando su contenido
leer = open('mi_archivo.txt', 'r')
contenido = leer.read()
print(contenido)
leer.close()





'''
Práctica Crear y Escribir Archivos 3
Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . 
Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en 
modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.
'''
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Abriendo el archivo en modo append ('a') para agregar contenido al final
a = open('registro.txt', 'a')
# Convirtiendo la lista en una cadena con tabuladores entre elementos
linea = '\t'.join(registro_ultima_sesion) + '\n'
# Escribiendo la cadena al final del archivo
a.write(linea)
a.close()

# Abriendo el archivo en modo lectura ('r') y mostrando su contenido
l = open('registro.txt', 'r')
contenido = l.read()
print(contenido)
l.close()













