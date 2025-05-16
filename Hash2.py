tabla_hash = {
    "apple": "manzana",
    "banana": "plátano",
    "orange": "naranja",
    "grape": "uva"
}

claves_a_buscar = ["banana", "grape", "melon", "apple", "kiwi"]

print("Búsqueda de traducciones usando tabla hash:\n")

for clave in claves_a_buscar:
    if clave in tabla_hash:
        print(f"La traducción de '{clave}' es '{tabla_hash[clave]}'.")
    else:
        print(f"No se encontró la traducción para '{clave}'.")
