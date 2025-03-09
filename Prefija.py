def evaluar_prefija(expresion):
    pila = []
    tokens = reversed(expresion.split()) 
    for token in tokens:
        if token.isdigit():
            pila.append(int(token))
        else:
            a = pila.pop()
            b = pila.pop()
            if token == '+': pila.append(a + b)
            elif token == '-': pila.append(a - b)
            elif token == '*': pila.append(a * b)
            elif token == '/': pila.append(a / b)
    
    return pila[0]

exp_prefija = "* + 3 4 2"
print(evaluar_prefija(exp_prefija))  
