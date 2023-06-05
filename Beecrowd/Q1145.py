n,n2 = map(int,input().split(" "))
i = 1
q = i
while q < (n2 - 3):
    j = i
    q = i
    print(f"{i} {j+1} {q+2}")
    i+=3