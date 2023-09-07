t = int(input())
i = 0
numeros = []

n = input()
x = n.split()

numeros = list(map(int, x))


numeros.sort()
i = int(t/2)
if t%2 != 0:
    mediana = numeros[i]

else:
    r = (numeros[i] + numeros[i - 1]) / 2
    mediana = r

print(mediana)