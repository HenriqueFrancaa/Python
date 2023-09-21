
n = int(input())
b = 0
p = 0
t = True
i = 0
if n%2 == 0:
    while i < n:
        j = 0
        while j < n:
            if j == n-1:
                if t == True:
                    b+=1
                else:
                    p+=1
                t = t
            elif t == True:
                b+=1
                t = False
            elif t == False:
                p+=1
                t = True
            j+=1

        i+=1

else:
    while i < n:
        j = 0
        while j < n:
            if t == True:
                b+=1
                t = False
            else:
                p+=1
                t = True
            j+=1
        i+=1

print(f"{b} casas brancas e {p} casas pretas")