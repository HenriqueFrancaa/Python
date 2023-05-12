dosages, period, year = input().split(" ")

dosages = int(dosages)
period = int(period)
year = int(year)
i = 0

while i < dosages:
    if i == dosages - 1:
        print(year, end=" ")
    else:
        print(year,end=", ")
    
    year = year + period
    
    i+=1