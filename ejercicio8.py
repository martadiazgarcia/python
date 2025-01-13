#Implementar una función que reciba una cadena y devuelva un diccionario con la cantidad de repeticiones de cada palabra en la cadena


def contar(texto):
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras


def repetida(palabras):
    palabra = ''
    frecuencia = 0
    for palab, frec in palabras.items():
        if frec > frecuencia:
            palabra = palab
            frecuencia = frec
    return palabra, frecuencia


print(contar('Estoy probando esta funcion por eso repito la palabra funcion'))
print(repetida(contar('Estoy probando esta funcion por eso repito la palabra funcion')))