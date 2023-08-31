

s = str(input())

sum = 0.0
cont = 0.0
for i in range(0,12):
    for j in range(0,12):
        n = float(input())
        if j < 11-i:
            sum += n
            cont+=1



avg = sum/cont

if s == 'S':
    print(f"{sum:.1f}")
else:
    print(f"{avg:.1f}")
