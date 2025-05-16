import matplotlib.pyplot as plt
import time

def visualizar_secuencial(lista, objetivo):
    for i in range(len(lista)):
        plt.clf()
        colores = ['blue'] * len(lista)
        colores[i] = 'red'  
        plt.bar(range(len(lista)), lista, color=colores)
        plt.title(f"Búsqueda Secuencial: Revisando índice {i}")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.pause(0.5)
        if lista[i] == objetivo:
            plt.title(f"¡Elemento encontrado en el índice {i}!")
            plt.bar(range(len(lista)), lista, color=colores)
            plt.show()
            return i
    plt.title("Elemento no encontrado")
    plt.show()
    return -1

lista = [5, 2, 9, 1, 5, 6]
objetivo = 9
visualizar_secuencial(lista, objetivo)
