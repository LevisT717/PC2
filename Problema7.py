def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

suma = 0
for num in range(2, 100):
    if es_primo(num):
        suma += num

print("La suma de todos los primos menores que 100 es:", suma)
