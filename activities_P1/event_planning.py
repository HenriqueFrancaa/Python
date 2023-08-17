p,o,h,s = map(int,input().split(" "))
menor_preco = 500000
i = 0

while i < h:
    preco_pessoa = int(input())
    j = 0
    c = input();
    camas = c.split()
    vetor = list(map(int, camas))
    tam = len(vetor);
    while j < tam:
        if vetor[j] >= p:
            custo = p * preco_pessoa
            if custo <= o and custo < menor_preco:
                menor_preco = custo
        j+=1    

    i+=1

if(menor_preco == 500000):
    print(f"stay home\n")
else:
    print(f"{menor_preco}")

