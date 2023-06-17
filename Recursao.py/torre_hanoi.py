def move(disco,origem,destino,auxilio):
    if disco >= 1:
        move(disco - 1, origem, auxilio, destino)
        print(f"Movendo da torre {origem} para a torre {destino}")
        move(disco - 1, auxilio, destino, origem ) 
        global jogadas
        jogadas += 1

jogadas = 0
n = int(input())
move(n,'A','C','B')
print(f"\nA quantidade de jogadas foi de {jogadas}")