# Problema 11 - Eliminar vocales de una cadena

def sin_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ""
    for char in texto:
        if char not in vocales:
            resultado += char
    return resultado

# Ejemplo de uso
entrada = input("Ingrese un texto: ")
print("Texto sin vocales:", sin_vocales(entrada))
