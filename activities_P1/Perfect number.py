testes = int(input())
i = 0


while i < testes:
    n = int(input())
    j = 1
    count = 0
    while j < n:
        if n%j == 0:
            count+=j
        j+=1

    if count == n:
        print(f"{n} eh perfeito")
    else:
        print(f"{n} nao eh perfeito")


    i += 1
