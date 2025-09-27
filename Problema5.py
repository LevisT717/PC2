numeros = []  # lista para guardar los números

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    
    if respuesta == "SI":
        num = int(input("Ingrese el número: "))
        numeros.append(num)
    elif respuesta == "NO":
        break
    else:
        print("⚠️ Respuesta inválida. Escriba 'SI' o 'NO'.")

# Contar pares e impares
pares = 0
impares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar resultados
print("\nNúmeros ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)