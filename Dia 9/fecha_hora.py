#import datetime
from datetime import datetime
from datetime import date
mi_hora = datetime(1799, 5, 5)
print(mi_hora)

nacimiento = date(1995, 3, 5)
defuncion = date(2095, 4, 19)
a = defuncion - nacimiento
print(a)

'''
Práctica Módulo Datetime 1
Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999
'''

# Crear un objeto de fecha para el 3 de febrero de 1999
mi_fecha = date(1999, 2, 3)
print(mi_fecha)



'''
Práctica Módulo Datetime 2
Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
'''

# Crear un objeto que almacene la fecha actual
hoy = date.today()

# Imprimir la fecha actual
print(hoy)



'''
Práctica Módulo Datetime 3
En una variable llamada minutos, almacena únicamente los minutos de la hora actual.

Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43
'''
# Obtener la hora actual
hora_actual = datetime.now()

# Obtener los minutos de la hora actual
minutos = hora_actual.minute

# Imprimir los minutos
print(minutos)








