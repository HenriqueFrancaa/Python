teste, saldo_total = map(int,input().split(" "))
menor = 10000
for i in range(1, teste+1):
    movimentacao = int(input())

    saldo = movimentacao + saldo_total

    if saldo < menor:
        menor = saldo
        
    
print(menor)
