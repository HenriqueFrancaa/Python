testes = int(input())

i = 0

while i < testes:
    n = int(input())
    j = 1
    count = 0
    while j <= n:
        if n%j == 0:
            count+=j
        j+=1
    
    if count == n+1:
        print(f"{n} eh primo")

    else:
        print(f"{n} nao eh primo")
    
    i+=1

    #Questão Beecrowd 1165 :)
    