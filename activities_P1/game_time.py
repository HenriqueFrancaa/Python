hi,mi,hf,mf = input().split(" ")
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

inicial_min = (hi * 60) + mi
final_min = (hf * 60) + mf

tempo = final_min - inicial_min

if tempo > 0:
    horas = tempo // 60
    minutos = tempo%60
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

else:
    if tempo <= 0:
        tempo = 24 *60 + tempo
        horas = tempo // 60
        minutos = tempo%60
        print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

