velocidade = float(input("sua velocidade em Km: "))
if velocidade > 80:
    print("MULTADO, você excedeu o limite de velocidade de 80 km/h")
    multa = (velocidade - 80) * 7
    print(f"Você pagará uma multa de R$ {multa:.2f}")
    print("tenha um bom dia e dirija com cuidado na próxima vez!")
if velocidade <= 80:
    print("Está dentro do limite")
    print(" \ntenha um bom dia e continue dirigindo com cuidado")
print("  \nAtenciosamente Detran")
