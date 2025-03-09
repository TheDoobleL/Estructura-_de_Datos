def evaluar_postfija(expresion):
    pila = []
    tokens = expresion.split()
    
    for token in tokens:
        if token.isdigit():
            pila.append(int(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+': pila.append(a + b)
            elif token == '-': pila.append(a - b)
            elif token == '*': pila.append(a * b)
            elif token == '/': pila.append(a / b)
    
    return pila[0]

exp_postfija = "3 4 + 2 *"
print(evaluar_postfija(exp_postfija))  
