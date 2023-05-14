while True:
    n1, n2 = input().split(" ")

    n1 = int(n1)
    n2 = int(n2)        

    # a questão consiste em saber qual é o maior ciclo que existe em um intervalo de dois números.
    # por exemplo se n1 = 1 e n2 = 10, concorda que existe uma distancia de 9 números até chegar o 10.
    # então seria preciso fazer o ciclo do 2, depois o de 3 e assim por diante, e qual desses vai ter o ciclo maior? eis a questão e qual é o tamanho do ciclo? é isso que vamos descobrir.

    maior_ciclo = 0
    i = 1
    numero = n1  # a variável número, vai ficar atualizando pra cada rodada do bloco, no caso do exemplo que eu falei, é como se ele fosse o numero 2 e depois virasse o 3 e assim por diante.

    while numero < n2:
        ciclo = 1 #ciclo está valendo 1, porque ele já está contando com o numero 1.

        while numero != 1:
            if numero%2 == 0:
                ciclo+=1
                numero = numero//2

            elif numero%2 != 0:
                ciclo+=1
                numero = numero*3 + 1

        numero = n1 + i
        i+=1

        if ciclo > maior_ciclo:
            maior_ciclo = ciclo  # aqui, em cada rodada de número, ele fica atualizando qual é o maior ciclo.

    print(maior_ciclo)


