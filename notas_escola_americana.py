nota = int(input())

if nota == 0:
    print("E")

elif nota > 0 and nota <= 35:
    print("D")

elif nota > 35 and nota <= 60:
    print("C")

elif nota > 60 and nota <= 85:
    print("B")

else:
    print("A")