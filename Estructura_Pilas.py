class Pila:
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.pila = []
        self.tope = 0

    def insertar(self, elemento):
        if self.tope < self.capacidad:
            self.pila.append(elemento)
            self.tope += 1
            self.dibujar_pila()
        else:
            print("Error: Desbordamiento de pila (Stack Overflow)")

    def eliminar(self):
        if self.tope > 0:
            elemento = self.pila.pop()
            self.tope -= 1
            self.dibujar_pila()
        else:
            print("Error: Subdesbordamiento de pila (Stack Underflow)")

    def dibujar_pila(self):
        print("Pila actual:")
        for i in range(len(self.pila) - 1, -1, -1):
            if i == self.tope - 1:
                print(f"[{self.pila[i]}] <- TOPE")
            else:
                print(f"[{self.pila[i]}]")
        
        if self.tope == 0:
            print("La pila está vacía.")
        
        print(f"Capacidad de la pila: {self.capacidad} - TOPE={self.tope}")
        print("-" * 30)  

pila = Pila()

print("Estado inicial:")
pila.dibujar_pila()  

pila.insertar("X")  
pila.insertar("Y")  
pila.eliminar()      
pila.eliminar()      
pila.eliminar()      
pila.insertar("V")  
pila.insertar("W")  
pila.eliminar()      
pila.insertar("R")  

pila.dibujar_pila()
