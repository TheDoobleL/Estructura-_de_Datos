def floyd(grafo):
    n = len(grafo)
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        for j, peso in grafo[i].items():
            dist[i][j] = peso

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

grafo = {
    0: {1: 3, 2: 6},
    1: {2: 2},
    2: {}
}

matriz_adyacencia = {
    0: {0: 0, 1: 3, 2: 6},
    1: {0: float('inf'), 1: 0, 2: 2},
    2: {0: float('inf'), 1: float('inf'), 2: 0}
}

distancias = floyd(matriz_adyacencia)
print("Distancias mínimas entre todos los pares de nodos:")
for fila in distancias:
    print(fila)

