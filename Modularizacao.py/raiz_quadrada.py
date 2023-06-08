def quadrada(n):
    r = 0
    i = 1
    while r < n:
        q = i
        r = i * q
        if r == n:
            n = i
        i = i + 1
    return(n)

numero = int(input("Digite um número pra ver a sua raiz quadrada: "))

raiz = quadrada(numero)
print(f"A raiz quadrada de {numero} é {raiz}")