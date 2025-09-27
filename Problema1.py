lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

lista_procesada = []
for num in lista_original:
    if num not in lista_procesada:
        lista_procesada.append(num)

print("Lista original:", lista_original)
print("Lista procesada:", lista_procesada)