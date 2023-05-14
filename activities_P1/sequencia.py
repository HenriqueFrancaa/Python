n1, n2 = map(int,input().split(" "))
	
maior_ciclo = 0
i = 0
numero = (n1+1) + i

while numero < n2:
    n = numero
    ciclo = 1
    while n != 1:
        if n%2 == 0:
            ciclo+=1
            n = n//2
        elif n%2 != 0:
            ciclo+=1
            n = n*3 + 1
    
    if ciclo > maior_ciclo:
        maior_ciclo = ciclo

print(maior_ciclo)


