elementos = [10, 23, 45, 70, 11, 15, 90, 100]

tabla_hash = set(elementos)

elementos_a_buscar = [70, 15, 99, 100, 5]

print("Búsqueda de elementos en la lista usando tabla hash:\n")

for elem in elementos_a_buscar:
    if elem in tabla_hash:
        print(f"El elemento {elem} SÍ está en la lista.")
    else:
        print(f"El elemento {elem} NO está en la lista.")
