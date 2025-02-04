pila = []

def apilar(elemento):
    pila.append(elemento)
    print(f"Elemento '{elemento}' apilado. Pila actual: {pila}")

def desapilar():
    if len(pila) == 0:
        print("La pila está vacía, no se puede desapilar.")
    else:
        elemento = pila.pop()
        print(f"Elemento '{elemento}' desapilado. Pila actual: {pila}")

def cima():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print(f"Elemento en la cima: {pila[-1]}")

apilar(10)
apilar(20)
apilar(30)

cima()

desapilar()
desapilar()

cima()

desapilar()
desapilar()
