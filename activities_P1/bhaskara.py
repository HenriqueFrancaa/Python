import math
a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

delta = b**2 - 4 * a * c

if delta < 0:
    print("Impossivel calcular")

else:
    if a == 0:
        print("Impossivel calcular")
    else:
        if delta > 0:
            r1 = (-b + math.sqrt(delta)) / (2 * a)
            r2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f"R1 = {r1:.5f}")
            print(f"R2 = {r2:.5f}")

