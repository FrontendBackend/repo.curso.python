import os
import shutil
import send2trash


#archivo = open('curso.txt', 'a')
#archivo.write('texto en prueba')
#archivo.close()
print(os.listdir())

#shutil.move('curso.txt', 'C:\\Users\\jvale\\Desktop')

print(os.walk('C:\\Users\\jvale\\Desktop'))

ruta = 'C:\\Users\\jvale\\Desktop\\adjuntar'
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')

    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')

    print('Los archivos son:')
    for arch in archivo:
        if arch.startswith('2015'):
            print(f'\t{arch}')
    print('\n')





