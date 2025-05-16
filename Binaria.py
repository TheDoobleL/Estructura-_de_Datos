import matplotlib.pyplot as plt
import time

def visualizar_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        plt.clf()
        colores = ['blue'] * len(lista)
        for i in range(inicio, fin+1):
            colores[i] = 'yellow' 
        medio = (inicio + fin) // 2
        colores[medio] = 'red' 
        plt.bar(range(len(lista)), lista, color=colores)
        plt.title(f"Búsqueda Binaria: Revisando índice {medio}")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.pause(0.7)
        if lista[medio] == objetivo:
            plt.title(f"¡Elemento encontrado en el índice {medio}!")
            plt.bar(range(len(lista)), lista, color=colores)
            plt.show()
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    plt.title("Elemento no encontrado")
    plt.show()
    return -1

lista_ordenada = sorted([5, 2, 9, 1, 5, 6])
objetivo = 5
visualizar_binaria(lista_ordenada, objetivo)
