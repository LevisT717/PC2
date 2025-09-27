# Problema 10 - Función para calcular el factorial de un número

def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso
num = int(input("Ingrese un número entero no negativo: "))
print(f"El factorial de {num} es: {factorial(num)}")
