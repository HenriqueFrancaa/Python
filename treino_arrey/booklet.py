
while True:
    
    paginas = int(input())

    if paginas == 0:
        break

    paginas_pares = []
    paginas_impares = []

    for i in range(0,paginas):
        i += 1
        if i%2 == 0:
            paginas_pares.append(i)
        else:
            paginas_impares.append(i)
    
    print(f"Printing order for {paginas} pages:")
    if paginas == 1:
        print(f"Sheet 1, front: Blank, 1")
    
    else:
        if (paginas+1)%4 == 0:
            paginas_pares.append("Blank")
            paginas += 1

        if (paginas + 2)%4 == 0:
            paginas_pares.append("Blank")
            paginas_impares.append("Blank")
            paginas += 2

        if (paginas + 3)%4 == 0:
            paginas_pares.append("Blank")
            paginas_pares.append("Blank")
            paginas_impares.append("Blank")
            paginas += 3
    
    
    
    
        for j in range(paginas//4):
            print(f"Sheet {j+1}, front: {paginas_pares[-1]}, {paginas_impares[0]}")
            print(f"Sheet {j+1}, back : {paginas_pares[0]}, {paginas_impares[-1]}")
            paginas_pares.pop(0)
            paginas_pares.pop(-1)
            paginas_impares.pop(0)
            paginas_impares.pop(-1)
    
    
    


