'''
Práctica Abrir y Manipular Archivos 1
Abre el archivo texto.txt e imprime su contenido.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
'''
# Abre el archivo en modo lectura ('r')
with open('prueba.txt', 'r') as archivo:
    # Lee todo el contenido del archivo
    contenido = archivo.read()
    # Imprime el contenido del archivo
    print(contenido)
    archivo.close()


'''-----------Resultado alternativo---------------'''
r = open('prueba.txt')
contenido = r.read()
print(contenido)
r.close()




'''
Práctica Abrir y Manipular Archivos 2
Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
'''
r = open('prueba.txt')
contenido = r.readline()
print(contenido)

r.close()





'''
Práctica Abrir y Manipular Archivos 3
Abre el archivo texto.txt e imprime únicamente la segunda línea.
'''
r = open('prueba.txt')
contenido = r.readlines()
print(contenido[1])

r.close()










