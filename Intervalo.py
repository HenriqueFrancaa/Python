n1 = float(input())

if n1 > 25:
    if n1 <= 50:
        print("Intervalo (25,50]")

if n1 == 0:
    print("Intervalo [0,25]")

if n1 > 0:
    if n1 <= 25:
        print("Intervalo [0,25]")

if n1 > 50:
    if n1 <= 75:
        print("Intervalo (50,75]")

if n1 > 75:
    if n1 <= 100:
        print("Intervalo (75,100]")

if n1 > 100:
    print("Fora de intervalo")
    
else:
    if n1 < 0:
        print("Fora de intervalo")

