


while True:
    try:
        n1, n2 = input().split(" ")
    
        n1 = int(n1)
        n2 = int(n2)

        maior_ciclo = 0
        i = 1
        menor_numero = n1 

        maior_numero = (n1 + n2 + abs(n1 - n2)) / 2
        menor_numero = (n1 + n2 - abs(n1 - n2)) / 2

        while menor_numero <= maior_numero:
            ciclo = 1 

            while menor_numero != 1:
                if menor_numero%2 == 0:
                    ciclo+=1
                    menor_numero = menor_numero//2

                elif menor_numero%2 != 0:
                    ciclo+=1
                    menor_numero = menor_numero*3 + 1

            menor_numero = n1 + i
            i+=1

            if ciclo > maior_ciclo:
                maior_ciclo = ciclo  

        resultado = "{} {} {}".format(n1,n2,maior_ciclo)
        print(resultado)
    except EOFError:
        break