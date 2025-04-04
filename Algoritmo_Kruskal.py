class UnionFind:
    def __init__(self, elementos):
        self.padre = {e: e for e in elementos}
    
    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]
    
    def unir(self, x, y):
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        if raiz_x != raiz_y:
            self.padre[raiz_x] = raiz_y

def kruskal(grafo):
    aristas = []
    for u in grafo:
        for v, w in grafo[u].items():
            aristas.append((w, u, v))
    
    aristas.sort()
    uf = UnionFind(grafo.keys())
    mst = []
    
    for peso, u, v in aristas:
        if uf.encontrar(u) != uf.encontrar(v):
            uf.unir(u, v)
            mst.append((u, v, peso))
    
    return mst

grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

mst = kruskal(grafo)
print("Árbol de expansión mínima (MST):")
for arista in mst:
    print(arista)

