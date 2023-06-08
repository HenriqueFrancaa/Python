def somando(n1,n2):
    sum = n1 + n2
    return sum

def sub(n1,n2):
    subtracao = n1 - n2
    return subtracao

def multi(n1,n2):
    multiplicacao = n1 * n2
    return multiplicacao

def div(n1,n2):
    divisao = n1 / n2
    return divisao

numero1,numero2 = map(int,input("Digite dois números: ").split(" "))

soma = somando(numero1,numero2)
subtracao = sub(numero1,numero2)
multiplicacao = multi(numero1,numero2)
divisao = div(numero1,numero2)

print(f"SOMA : {soma}\nSUBTRAÇÂO : {subtracao}\nMULTIPLICAÇÂO : {multiplicacao}\nDIVISÂO: {divisao}")