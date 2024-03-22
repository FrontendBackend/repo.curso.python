'''
Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan,
y devuelva esa cantidad como resultado.
'''
def cantidad_atributos (**kwargs):
    return len(kwargs)

# Ejemplo de uso
resultado = cantidad_atributos(a=1, b=2, c=3)
print(resultado)  # Output: 3





'''
Práctica sobre Argumentos Indefinidos (**kwargs) 2
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en 
forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
'''
def lista_atributos(**kwargs):
    return list(kwargs.values())

# Ejemplo de uso
resultado = lista_atributos(a=1, b=2, c=3)
print(resultado)  # Output: [1, 2, 3]





'''
Práctica sobre Argumentos Indefinidos (**kwargs) 3
Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de 
argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
'''
def describir_persona(nombre, **kwargs):

    caracteristica = (f'Características de {nombre}: \n color de ojos: {kwargs["color_ojos"]} \n color de pelo: {kwargs["color_pelo"]}')
    return caracteristica

resultado = describir_persona("Yngrid", color_ojos="Café", color_pelo="Negro")
print(resultado)

'''----------------resultado alternativo----------------'''
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for atributo, valor in kwargs.items():
        print(f"{atributo}: {valor}")

# Ejemplo de uso
describir_persona("María", color_ojos="azules", color_pelo="rubio")




