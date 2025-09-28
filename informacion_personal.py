informacion_personal = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}
print("diccionario inicial:", informacion_personal)

informacion_personal["ciudad"] = "Guayaquil"
print("diccionario modificado 'ciudad':", informacion_personal)

informacion_personal["profesion"] = "Desarrollador de Software"
print("diccionario modificado 'profecion':", informacion_personal)

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"
print("diccionario modificado 'telefono':", informacion_personal)

informacion_personal.pop("edad")
print("diccionario modificado 'edad':", informacion_personal)

print("\nDiccionario final:", informacion_personal)


