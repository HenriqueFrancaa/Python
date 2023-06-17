def calculate_cycle_size(number):
    ciclo = 1
    while number != 1:
        if number%2 == 0:
            number = number/2
        else:
            number = number * 3 + 1
        ciclo+=1
        return(ciclo)


def calculate_max_cycle(start,end):
    maior = 0
    ciclo = 0
    while start <= end:
        ciclo = calculate_cycle_size(start)
        if ciclo > maior:
            maior = ciclo
        start+=1
        return(maior)

n1,n2 = input().split(" ")
n1 = int(n1)
n2 = int(n2)

if n1 > n2:
    q = n1
    n1 = n2
    n2 = q

maior_ciclo = calculate_max_cycle(n1,n2)

print(maior_ciclo)