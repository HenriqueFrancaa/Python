def ciclo(numero):
    cycle = 1
    n = numero
    while n != 1:
        if n%2 == 0:
            n = n/2
        else:
            n = n * 3 + 1
        cycle+=1
    return(cycle)

def max_cycle(n1,n2):
    maior = 0
    numero = n1
    cycle = 0
    while numero <= n2:
        cycle = ciclo(numero)
        if cycle > maior:
            maior = cycle
        numero+=1
    return(maior)

n1,n2 = map(int,input().split(" "))

if n1 > n2:
    q = n1
    n1 = n2
    n2 = q

maior = max_cycle(n1,n2)

print(maior)