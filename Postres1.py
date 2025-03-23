class Postre:
    def __init__(self, nombre, ingredientes=None):
        self.nombre = nombre
        self.ingredientes = ingredientes if ingredientes else []
    
    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
    
    def eliminar_ingrediente(self, ingrediente):
        if ingrediente in self.ingredientes:
            self.ingredientes.remove(ingrediente)
    
    def mostrar_ingredientes(self):
        print(f"Ingredientes de {self.nombre}: {', '.join(self.ingredientes) if self.ingredientes else 'No tiene ingredientes'}")

class GestionPostres:
    def __init__(self):
        self.postres = [
            Postre("Pastel de Chocolate", ["Harina", "Azúcar", "Cacao", "Huevo", "Leche"]),
            Postre("Flan", ["Leche", "Azúcar", "Huevo", "Vainilla"]),
            Postre("Gelatina", ["Agua", "Grenetina", "Azúcar", "Saborizante"])
        ]
        self.eliminar_duplicados()
    
    def eliminar_duplicados(self):
        nombres_unicos = set()
        postres_unicos = []
        for postre in self.postres:
            if postre.nombre.lower() not in nombres_unicos:
                nombres_unicos.add(postre.nombre.lower())
                postres_unicos.append(postre)
        self.postres = postres_unicos
    
    def buscar_postre(self, nombre):
        for postre in self.postres:
            if postre.nombre.lower() == nombre.lower():
                return postre
        return None
    
    def agregar_postre(self, nombre):
        if self.buscar_postre(nombre) is None:
            self.postres.append(Postre(nombre))
            self.postres.sort(key=lambda p: p.nombre.lower())
            print("Postre agregado.")
        else:
            print("El postre ya existe.")
    
    def eliminar_postre(self, nombre):
        postre = self.buscar_postre(nombre)
        if postre:
            self.postres.remove(postre)
            print("Postre eliminado.")
        else:
            print("El postre no existe.")
    
    def agregar_ingrediente(self, nombre_postre, ingrediente):
        postre = self.buscar_postre(nombre_postre)
        if postre:
            postre.agregar_ingrediente(ingrediente)
            print("Ingrediente agregado.")
        else:
            print("El postre no existe.")
    
    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        postre = self.buscar_postre(nombre_postre)
        if postre:
            postre.eliminar_ingrediente(ingrediente)
            print("Ingrediente eliminado.")
        else:
            print("El postre no existe.")
    
    def mostrar_ingredientes(self, nombre_postre):
        postre = self.buscar_postre(nombre_postre)
        if postre:
            postre.mostrar_ingredientes()
        else:
            print("El postre no existe.")
    
    def mostrar_postres(self):
        print("Lista de postres en orden alfabético:")
        for postre in sorted(self.postres, key=lambda p: p.nombre.lower()):
            print(postre.nombre)

if __name__ == "__main__":
    gestion = GestionPostres()
    while True:
        print("\n1. Agregar postre")
        print("2. Eliminar postre")
        print("3. Agregar ingrediente")
        print("4. Eliminar ingrediente")
        print("5. Mostrar ingredientes de un postre")
        print("6. Mostrar lista de postres")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestion.agregar_postre(input("Ingrese el nombre del postre: "))
        elif opcion == "2":
            gestion.eliminar_postre(input("Ingrese el nombre del postre a eliminar: "))
        elif opcion == "3":
            gestion.agregar_ingrediente(input("Ingrese el nombre del postre: "), input("Ingrese el ingrediente: "))
        elif opcion == "4":
            gestion.eliminar_ingrediente(input("Ingrese el nombre del postre: "), input("Ingrese el ingrediente a eliminar: "))
        elif opcion == "5":
            gestion.mostrar_ingredientes(input("Ingrese el nombre del postre: "))
        elif opcion == "6":
            gestion.mostrar_postres()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
