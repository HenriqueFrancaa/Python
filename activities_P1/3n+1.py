while True:
    n1,n2 = input().split(" ")
    n1 = int(n1)
    n2 = int(n2)
    maior_ciclo = 0
    for numero in range(n1+1,n2):
        n = numero
        ciclo = 1
        while n != 1:
            if n%2 == 0:
                ciclo+=1
                n = n//2
            elif n%2 != 0:
                ciclo+=1
                n = n*3 + 1
        
        if ciclo > maior_ciclo:
            maior_ciclo = ciclo
    
    resultado = "{} {} {}".format(n1,n2,maior_ciclo)

    print(resultado)

#Questao THE HUXLEY 407 :)

