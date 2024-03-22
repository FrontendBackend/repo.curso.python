'''
Práctica Manejo de Errores 1
Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. En el caso de este
ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado:
deberás implementarlo DENTRO de la función. En forma de comentario, verás un ejemplo de resolución. Ten presente,
sin embargo, que la forma preferida es la que hemos visto en clase.

Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error,
imprima en pantalla el mensaje: "Error inesperado". En caso contrario, deberá limitarse a mostrar el
resultado de la suma entre los dos números.
'''
def suma(num1, num2):
    try:
        resultado = num1 + num2
    except:
        print("Error inesperado")
    else:
        print(resultado)


# Ejemplos de uso
suma(5, 3)  # Salida esperada: La suma es: 8
suma("Hola", 5)  # Salida esperada: Error inesperado
suma(10, "Mundo")  # Salida esperada: Error inesperado


'''
Práctica Manejo de Errores 2
Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. 
En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente 
distinta para que pueda ser evaluado: deberás implementarlo DENTRO de la función. En forma de comentario, 
verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.

Implementa para la siguiente función cociente(), un manejador de errores:

Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"

Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: 
"El segundo argumento no debe ser cero"

En caso que no se produzca un error, deberá limitarse a imprimir el 
resultado del cociente (división) entre los dos números entregados como argumento.
'''

def cociente(num1, num2):
    try:
        resultado = num1 / num2
        print(resultado)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")



'''
Práctica Manejo de Errores 3
Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. 
En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta 
para que pueda ser evaluado: deberás implementarlo DENTRO de la función. En forma de comentario, 
verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.

Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():

En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), 
mostrar en pantalla el mensaje: "El archivo no fue encontrado"

En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"

Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"

En todos los casos, al finalizar, imprimir: "Finalizando ejecución"
'''

def abrir_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            print("Abriendo exitosamente")
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    finally:
        print("Finalizando ejecución")

# Probando
abrir_archivo("C:\\dev\\python\\app\\python\\Dia 8\\Manejo_de_errores.py")









