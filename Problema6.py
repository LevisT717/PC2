alumnos = []  # lista que almacenará todos los alumnos

# Definir cuántos alumnos se van a registrar
n = int(input("¿Cuántos alumnos desea registrar?: "))

for i in range(n):
    print(f"\nAlumno {i+1}:")
    nombre = input("Ingrese el nombre del alumno: ")
    
    notas = []  # lista para las 3 notas de cada alumno
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j+1}: "))
        notas.append(nota)
    
    # Crear un diccionario para cada alumno
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    
    # Agregar a la lista de alumnos
    alumnos.append(alumno)

# Mostrar listado completo
print("\nListado de alumnos y sus notas:")
for a in alumnos:
    print(f"Alumno: {a['Alumno']}, Notas: {a['Notas']}")