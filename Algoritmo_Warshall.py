def warshall(grafo):
    n = len(grafo)
    cierre = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in grafo[i]:
            cierre[i][j] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                cierre[i][j] = cierre[i][j] or (cierre[i][k] and cierre[k][j])
    
    return cierre

grafo = {
    0: [1],
    1: [2],
    2: []
}

cierre_transitivo = warshall(grafo)
print("Cierre transitivo del grafo:")
for fila in cierre_transitivo:
    print(fila)
