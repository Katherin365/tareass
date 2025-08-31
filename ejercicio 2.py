# Programa 2: Ordenación de Arreglo Multidimensional

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

matriz = [
    [34, 12, 25],
    [9,  5,  17],
    [42, 8,  19]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_ordenar = 1
matriz[fila_ordenar] = bubble_sort(matriz[fila_ordenar])

print("\nMatriz con la fila", fila_ordenar, "ordenada:")
for fila in matriz:
    print(fila)

