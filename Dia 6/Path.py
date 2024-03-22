from pathlib import Path
base = Path.home()
guia = Path(base,"Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
print(guia)
print(guia2)


guiaa = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guiaa.relative_to(Path("Europa"))
en_espania = guiaa.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)



'''
Práctica Path 1
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y utilizar el método home()
'''
from pathlib import Path
base = Path.home()
ruta_base0 = base

'''-------------resultado alternativo-------------------'''
# Almacena la ruta base del directorio del usuario
ruta_base = Path.home()

# Imprime la ruta base del directorio del usuario
print("Ruta base del directorio del usuario:", ruta_base)




'''
Práctica Path 2
Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
'''

from pathlib import Path

# Crear la ruta relativa
ruta = Path('Curso Python/Día 6/practicas_path.py')

# Imprimir la ruta relativa
print(ruta)






'''
Práctica Path 3
Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario.
'''
from pathlib import Path
base = Path.home()
ruta = Path(base,"Curso Python", "Día 6", "practicas_path.py")

print(ruta)


