# Trabajo con Archivos de Texto en Python

# 1. Escritura en el archivo
archivo = open("alumnos.txt", "w")  # "w" crea el archivo o sobrescribe si ya existe

# Escribimos varios nombres en el archivo
archivo.write("Michelle Estefany Toro Delgado\n")
archivo.write("Jhon Alejandro Gonzalez Parrales\n")
archivo.write("María Fernanda Castillo Cedeño\n")

# Cerramos el archivo después de escribir
archivo.close()

# 2. Lectura del archivo
archivo = open("alumnos.txt", "r")  # "r" abre el archivo en modo lectura

# Leemos línea por línea
print("Lista de alumnos:")
linea = archivo.readline()
while linea:
    print(linea.strip())   # strip() elimina espacios y saltos de línea extra
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
