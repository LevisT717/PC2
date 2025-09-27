# Problema 8 - Serie de Fibonacci entre 0 y 50

a, b = 0, 1  # Los dos primeros números de la serie

print("Serie de Fibonacci entre 0 y 50:")
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b
