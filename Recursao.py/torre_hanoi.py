def jogadas(j):
    if p == 1:
        return 1
    return 2**j - 1

p = int(input("Digite a quantidade de peças com que deseja jogar: "))

j = jogadas(p)

print(f"O número de movimentos minimos é de {j}")
#Jogo da torre de hanoi usando recursão
