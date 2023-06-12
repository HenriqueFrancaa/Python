def fat(n):
    if n == 0:
        return 1
    return(n * fat(n-1))

n = int(input())

fatorial = fat(n)
print(fatorial)