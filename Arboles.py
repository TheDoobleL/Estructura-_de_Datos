class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor, padre=None):
        nuevo_nodo = Nodo(valor)
        if not self.raiz and not padre:
            self.raiz = nuevo_nodo
            return True    
        padre_nodo = self.buscar(padre) if padre else self.raiz
        if padre_nodo:
            padre_nodo.hijos.append(nuevo_nodo)
            return True
        return False
    
    def buscar(self, valor, nodo=None):
        if not nodo:
            nodo = self.raiz
        if nodo.valor == valor:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self.buscar(valor, hijo)
            if encontrado:
                return encontrado
        return None
    
    def eliminar(self, valor):
        if self.raiz.valor == valor:
            self.raiz = None
            return True
        padre = self._buscar_padre(valor)
        if padre:
            for i, hijo in enumerate(padre.hijos):
                if hijo.valor == valor:
                    del padre.hijos[i]
                    return True
        return False
    
    def _buscar_padre(self, valor, nodo=None):
        if not nodo:
            nodo = self.raiz
        for hijo in nodo.hijos:
            if hijo.valor == valor:
                return nodo
            encontrado = self._buscar_padre(valor, hijo)
            if encontrado:
                return encontrado
        return None
    
    def preorden(self, nodo=None):
        if not nodo:
            nodo = self.raiz
        print(nodo.valor, end=' ')
        for hijo in nodo.hijos:
            self.preorden(hijo)
    
    def postorden(self, nodo=None):
        if not nodo:
            nodo = self.raiz
        for hijo in nodo.hijos:
            self.postorden(hijo)
        print(nodo.valor, end=' ')
    
    def por_niveles(self):
        if not self.raiz:
            return
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            print(nodo.valor, end=' ')
            cola.extend(nodo.hijos)
    
    def altura(self, nodo=None):
        if not nodo:
            if not self.raiz:
                return 0
            nodo = self.raiz
        if not nodo.hijos:
            return 1
        return 1 + max(self.altura(hijo) for hijo in nodo.hijos)
    
    def __str__(self, nodo=None, prefijo="", es_ultimo=True):
        if not nodo:
            if not self.raiz:
                return "Árbol vacío"
            return self.__str__(self.raiz)
        
        resultado = ""
        if nodo == self.raiz:
            resultado += f"{nodo.valor}\n"
        else:
            resultado += f"{prefijo}{'└─ ' if es_ultimo else '├─ '}{nodo.valor}\n"
        
        nuevos_prefijos = prefijo + ("    " if es_ultimo else "│   ")
        for i, hijo in enumerate(nodo.hijos):
            es_ultimo_hijo = i == len(nodo.hijos) - 1
            resultado += self.__str__(hijo, nuevos_prefijos, es_ultimo_hijo)
        
        return resultado

if __name__ == "__main__":
    arbol = Arbol()
    arbol.agregar("A")    
    arbol.agregar("B", "A")  
    arbol.agregar("C", "A")  
    arbol.agregar("D", "B")  
    arbol.agregar("E", "B")  
    arbol.agregar("F", "C")  

    print("Estructura del árbol:")
    print(arbol)

    print("\nRecorrido Preorden:")
    arbol.preorden()
    
    print("\n\nRecorrido por niveles:")
    arbol.por_niveles()
    
    print("\n\nAltura del árbol:", arbol.altura())
*
