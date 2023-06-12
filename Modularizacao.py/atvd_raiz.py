def quadrada(c):
    numero = c
    raiz_quadrada = 0.5 *(numero + numero/numero)
    return(raiz_quadrada)


numero = float(input())

raiz = quadrada(numero)

print(f"a raiz quadrada de {numero} é : {raiz:.6f}")