quantidade = int(input())
marcado = 0
futuro = 0
for i in range(1, quantidade + 1):
    numero = int(input())
    atual = numero
    

    if atual == futuro:
        marcado += 0
    if atual != futuro:
        marcado += 1
    
    futuro = atual
    atual = futuro

print(marcado) 


    
    