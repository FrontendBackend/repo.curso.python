import zipfile
import shutil

'''
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()
'''
# Descomprimir el archivo
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()


# Comprimir la carpeta
carpeta_origen = 'C:\\Users\\jvale\\Desktop\\adjuntar\\formatos'
archivo_destino = 'Todo_Comprimido'
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

# Descomprimir la carpeta
shutil.unpack_archive('Todo_Comprimido.zip', 'Extraccion Terminada', 'zip')