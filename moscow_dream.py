f,m,d,n = input().split(" ")
f = int(f)
m = int(m)
d = int(d)
n = int(n)

if f==0 or m==0 or d==0 or n<3:
    print("NO")

elif f+m+d < n:
    print("NO")
    
elif f+m+d >= n:
    print("YES")