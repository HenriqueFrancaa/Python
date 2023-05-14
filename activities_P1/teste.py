


while True:
    try:
        n1, n2 = input().split(" ")
    
        n1 = int(n1)
        n2 = int(n2)

        maior_ciclo = 0
        i = 1
        
        if n1 > n2:
            numero = n2
            maior = n1
            while numero <= maior:
                ciclo = 1 

                while numero != 1:
                    if numero%2 == 0:
                        ciclo+=1
                        numero = numero//2

                    elif numero%2 != 0:
                        ciclo+=1
                        numero = numero*3 + 1

            numero = n1 + i
            i-=1

            if ciclo > maior_ciclo:
                maior_ciclo = ciclo
        
        elif n2 > n1:
            numero = n1
            maior = n2

            while numero <= maior:
                ciclo = 1 

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
                maior_ciclo = ciclo  

        resultado = "{} {} {}".format(n1,n2,maior_ciclo)
        print(resultado)
    except EOFError:
        break