def fatorial(n):
    f = 1
    while n != 1:
        f *= n
        n = n - 1
    return f

def dobroo(n):
    d = n * 2
    return d

def triploo(n):
    t = n * 3
    return(t)

numero = int(input("Digite um numero para ver seu fatorial: "))
fat = fatorial(numero)
dobro = dobroo(numero)
triplo = triploo(numero)
print(f"O fatorial de {numero} é {fat}\nO dobro de {numero} é {dobro}\nO triplo de {numero} é {triplo}")
