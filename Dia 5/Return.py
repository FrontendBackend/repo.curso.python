'''
Práctica Return 1
Crea una función llamada potencia que tome dos valores numéricos como argumentos.
Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:
'''
def potencia(base, exponente):
    resultado = base**exponente
    print(resultado)
    return resultado

base = 3
exponente = 4




'''
Práctica Return 2

- Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), 
y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

- Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.

Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros.
'''
def usd_a_eur(dolares):
    euros = dolares * 0.90
    return euros
dolares = 50





'''
Práctica Return 3
Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, 
invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como 
argumento a la función creada.

Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.
'''
def invertir_palabra(palabra):
    palabra_invertida = palabra[::-1]  # Invertir la palabra utilizando slicing
    palabra_invertida_mayusculas = palabra_invertida.upper()  # Convertir la palabra invertida a mayúsculas
    return palabra_invertida_mayusculas

# Definir la variable palabra con el string deseado
palabra = "Python"

# Llamar a la función invertir_palabra y mostrar el resultado
print(invertir_palabra(palabra))











