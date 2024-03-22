'''
Práctica Archivos y Funciones 1
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro,
y devuelva su contenido (read).
'''
def abrir_leer(a):
    archivo = open(a)
    leer = archivo.read()
    return leer

print(abrir_leer("registro.txt"))



'''
Práctica Archivos y Funciones 2
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
'''
def sobrescribir(a):
    # Abrir el archivo en modo escritura ('w') para sobrescribir el contenido
    arc = open(a, 'w')
    # Escribir el texto "contenido eliminado"
    s = "contenido eliminado"
    sobreescribir = arc.write(s)
    return sobreescribir

# Ejemplo de uso de la función sobrescribir
print(sobrescribir("Prueba.txt"))



'''

Práctica Archivos y Funciones 3
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo 
una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
'''

def registro_error(archivo):
    abri_archivo = open(archivo, 'a')
    texto = "se ha registrado un error de ejecución"
    ejecutar = abri_archivo.writelines([texto])
    return ejecutar

print(registro_error("registro.txt"))















