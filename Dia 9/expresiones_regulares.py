'''
Práctica Módulo RE 1
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta,
que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio)
y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional,
tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok",
pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario
"La dirección de email es incorrecta" imprimiendo el mensaje.
'''
import re

def verificar_email(email):
    # Define el patrón de la expresión regular para verificar el email
    patron = r'^\S+@\S+\.(com|com\.br)$'

    # Utiliza re.match para buscar el patrón en el email
    if re.match(patron, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

# Ejemplo de uso
verificar_email("usuario@example.com")
verificar_email("usuario@example.com.br")
verificar_email("usuarioexample.com")
'''
En este código:

^ y $         -> aseguran que la expresión regular coincida con toda la cadena desde el principio hasta el final.
\S+           -> coincide con uno o más caracteres que no son espacios en blanco.
@             -> coincide con el símbolo "@".
\.            -> coincide con el punto literal.
(com|com\.br) -> coincide con "com" o "com.br".
re.match()    -> verifica si el patrón coincide con el email dado.
'''



'''
Práctica Módulo RE 2
Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra 
"Hola". Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", 
pero si detecta que la frase no contiene "Hola", debe informarle al usuario 
"No has saludado" imprimiendo el mensaje en pantalla.
'''
def verificar_saludo(frase):
    # Define el patrón de la expresión regular para verificar el saludo
    patron = r'^Hola\b'

    # Utiliza re.match para buscar el patrón al principio de la frase
    if re.match(patron, frase):
        print("Ok")
    else:
        print("No has saludado")

# Ejemplo de uso
verificar_saludo("Hola, ¿cómo estás?")
verificar_saludo("Buenos días, ¿qué tal?")
'''
En este código:

^           -> asegura que la expresión regular coincida con el inicio de la cadena.
Hola        -> coincide con la palabra "Hola".
\b          -> coincide con el límite de una palabra.
re.match()  -> verifica si el patrón coincide con la frase dada.
'''



'''
Práctica Módulo RE 3
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y 
cuatro numéricos a continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para 
comprobar si el código postal pasado como argumento sigue este patrón. Si el patrón es correcto, 
mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
'''
def verificar_cp(cp):
    # Define el patrón de la expresión regular para verificar el código postal
    patron = r'^[A-Za-z]{2}\d{4}$'

    # Utiliza re.match para buscar el patrón en el código postal
    if re.match(patron, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

# Ejemplo de uso
verificar_cp("AB1234")
verificar_cp("XYZ789")

'''
En este código:

^               -> asegura que la expresión regular coincida con el inicio de la cadena.
[A-Za-z]{2}     -> coincide con dos caracteres alfabéticos (mayúsculas o minúsculas).
\d{4}           -> coincide con cuatro dígitos numéricos.
$               -> asegura que la expresión regular coincida con el final de la cadena.
re.match()      -> verifica si el patrón coincide con el código postal dado.
'''