
codigo, quantidade = input().split(" ")
codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
    valor = 4.00
    total = valor * quantidade
    print(f"Total: R$ {total:.2f}")

if codigo == 2:
    valor = 4.50
    total = valor * quantidade
    print(f"Total: R$ {total:.2f}")

if codigo == 3:
    valor = 5.00
    total = valor * quantidade
    print(f"Total: R$ {total:.2f}")

if codigo == 4:
    valor = 2.00
    total = valor * quantidade
    print(f"Total: R$ {total:.2f}")
if codigo == 5:
    valor = 1.50
    total = valor * quantidade
    print(f"Total: R$ {total:.2f}")