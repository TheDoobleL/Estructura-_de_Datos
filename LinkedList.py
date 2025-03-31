class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            return
        ultimo = self.cabeza
        while (ultimo.siguiente):
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo_nodo

    def agregar_en_posicion(self, dato, posicion):
        if posicion < 0:
            print("Posición inválida")
            return
        if posicion == 0:
            self.agregar_al_inicio(dato)
            return
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        for i in range(posicion - 1):
            if actual is None:
                print("Posición fuera de rango")
                return
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_al_inicio(self):
        if self.esta_vacia():
            return
        self.cabeza = self.cabeza.siguiente

    def eliminar_al_final(self):
        if self.esta_vacia():
            return
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente
        actual.siguiente = None

    def eliminar_por_valor(self, valor):
        if self.esta_vacia():
            return
        if self.cabeza.dato == valor:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        anterior = None
        while actual and actual.dato != valor:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            return  
        anterior.siguiente = actual.siguiente

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.dato == valor:
                return True
            actual = actual.siguiente
        return False

    def tamano(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def imprimir_lista(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(' -> '.join(elementos))

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar_al_inicio(3)
lista.agregar_al_inicio(2)
lista.agregar_al_inicio(1)
lista.agregar_al_final(4)
lista.imprimir_lista()  
print("Tamaño de la lista:", lista.tamano())  
print("¿El valor 3 está en la lista?", lista.buscar(3))  
lista.eliminar_al_inicio()
lista.eliminar_al_final()
lista.imprimir_lista()  
lista.eliminar_por_valor(2)
lista.imprimir_lista()  

