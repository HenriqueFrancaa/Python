x,b = map(int,input().split(" "))

if x == 1:
    print(b)

elif x > 1:
    i = 1
    n = b
    while i < x:
        mult = 0
        mult = b * n
        b = mult
        i += 1
    print(b)

elif x == 0:
    print('1')

elif x < 0:
    i = 1
    n = b
    x = -(x)
    while i < x:
        mult = 0
        mult = b * n
        b = mult
        i+=1
    
    b = 1/b
    print(b)
