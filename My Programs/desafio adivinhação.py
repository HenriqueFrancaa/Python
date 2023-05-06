from random import randint #aleatorio
computador = randint(0,5) #vai fazer o computador pensar em um número aleatorio
print("Olá usuário, tudo bem?")
print("tenho um desafio pra você")
print("irei pensar em um número de 0 a 5 e você tem que tentar adivinhar")
print ("=+=" *10) # vai fazer a divisão da linha do jogo
palpite = int(input("qual número estou pensando? ")) #jogador tenta adivinhar
if palpite == computador:
    print("PARABÉNS, você ganhou")
if palpite != computador:
    print("PERDEU KKKKKKKKKKKKK")
    print(f"eu estava pensando no {computador} e não no {palpite}")
print("fim do desafio")

