quantity = int(input())
pay = 0
for i in range(quantity):
    codi,unity = map(int,input().split(" "))


    if codi == 1001:
        value = 1.50
        total_value = value * unity

    elif codi == 1002:
        value = 2.50
        total_value = value * unity

    elif codi == 1003:
        value = 3.50
        total_value = value * unity

    elif codi == 1004:
        value = 4.50
        total_value = value * unity

    elif codi == 1005:
        value = 5.50
        total_value = value * unity

    total = total_value
    pay += total

print(f"{pay:.2f}")
