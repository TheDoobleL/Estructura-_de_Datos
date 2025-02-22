def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

n = int(input("Capture un número para calcular su factorial: "))
if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    print(f"El factorial de {n} es {factorial_recursivo(n)}")
