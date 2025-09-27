# Problema 9 - Números perfectos menores que 1000

def es_perfecto(n):
    suma = 0
    for i in range(1, n):  # divisores propios menores que n
        if n % i == 0:
            suma += i
    return suma == n

print("Números perfectos menores que 1000:")
for num in range(1, 1000):
    if es_perfecto(num):
        print(num)
