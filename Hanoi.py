import tkinter as tk

class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        return self.items.pop() if self.items else None
    
    def ver_tope(self):
        return self.items[-1] if self.items else None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def obtener_elementos(self):
        return self.items[:]

class TorresHanoi:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Torres de Hanoi")
        self.canvas = tk.Canvas(raiz, width=600, height=400, bg="white")
        self.canvas.pack()
        
        self.torres = {"A": Pila(), "B": Pila(), "C": Pila()}
        self.discos = 5
        for i in range(self.discos, 0, -1):
            self.torres["A"].apilar(i)
        
        self.origen = None
        self.dibujar_torres()
        
        self.canvas.bind("<Button-1>", self.seleccionar_torre)
    
    def dibujar_torres(self):
        self.canvas.delete("all")
        posiciones = {"A": 100, "B": 300, "C": 500}
        for torre, pila in self.torres.items():
            x = posiciones[torre]
            self.canvas.create_rectangle(x - 10, 150, x + 10, 350, fill="black")
            elementos = pila.obtener_elementos()
            y = 340
            for disco in elementos:
                ancho = disco * 20
                self.canvas.create_rectangle(x - ancho, y, x + ancho, y + 20, fill="blue")
                y -= 20
        self.raiz.update()
    
    def seleccionar_torre(self, evento):
        posiciones = {"A": 100, "B": 300, "C": 500}
        for torre, x in posiciones.items():
            if x - 50 < evento.x < x + 50:
                if self.origen is None:
                    if not self.torres[torre].esta_vacia():
                        self.origen = torre
                else:
                    if self.origen != torre:
                        if self.torres[torre].esta_vacia() or self.torres[torre].ver_tope() > self.torres[self.origen].ver_tope():
                            self.mover_disco(self.origen, torre)
                    self.origen = None
                break
    
    def mover_disco(self, origen, destino):
        disco = self.torres[origen].desapilar()
        self.torres[destino].apilar(disco)
        self.dibujar_torres()

raiz = tk.Tk()
app = TorresHanoi(raiz)
raiz.mainloop()
