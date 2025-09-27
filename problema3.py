
numeros = []

for n in range(1500, 2701):  # 2701 porque el rango excluye el último número
    if n % 7 == 0 and n % 5 == 0:
        numeros.append(n)

print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:")
print(numeros)