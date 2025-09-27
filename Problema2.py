tipos_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Solicitar nombre del archivo
archivo = input("Nombre del archivo: ").strip().lower()

# Extraer la extensión (si existe)
if "." in archivo:
    extension = "." + archivo.split(".")[-1]  # toma lo que está después del último punto
else:
    extension = ""

# Buscar en el diccionario o usar el valor por defecto
tipo = tipos_mime.get(extension, "application/octet-stream")

print("Tipo MIME:", tipo)