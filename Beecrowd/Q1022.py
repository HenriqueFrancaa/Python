import math
testes = int(input())
j = 0
while j < testes:
    n1,barra,d1,op,n2,barra,d2 = input().split(" ")

    n1 = int(n1)
    d1 = int(d1)
    op = str(op)
    n2 = int(n2)
    d2 = int(d2)
    i = 1

    if op == '+':
        numerador = (n1 * d2) + (n2 * d1)
        denominador = d1 * d2

    elif op == '-':
        numerador = (n1 * d2) - (n2 * d1) 
        denominador = d1 * d2

    elif op == '*':
        numerador = n1 *n2
        denominador = d1 * d2

    elif op == '/':
        numerador = n1 * d2
        denominador = n2 * d1

    numerador2 = numerador
    denominador2 = denominador
    while denominador2 != 0:
        numerador2, denominador2 = denominador2, numerador2 %denominador2
    gdc = numerador2

    simp_num = numerador//gdc
    simp_den = denominador // gdc


    print(f"{numerador}/{denominador} = {simp_num}/{simp_den}")

    j+=1