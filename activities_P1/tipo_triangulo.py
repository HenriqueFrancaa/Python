x,y,z = input().split(" ")
x = float(x)
y = float(y)
z = float(z)

if x >= y and x >= z:
    a = x
    b = y
    c = z

if y >= x and y >= z:
    a = y
    b = x
    c = z

if z >= x and z >= y:
    a = z
    b = x
    c = y

if a >= b + c:
    print("NAO FORMA TRIANGULO")

else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")

    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
        if a == b != c or b == c != a or a == c != b:
            print("TRIANGULO ISOSCILIS")
        if a == b == c:
            print("TRIANGULO EQUILATERO")
    
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
        if a == b != c or b == c != a or a == c != b:
            print("TRIANGULO ISOSCILIS")
        if a == b == c:
            print("TRIANGULO EQUILATERO")