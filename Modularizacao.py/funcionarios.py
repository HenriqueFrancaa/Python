def cadastrar(nome,data_nascimento,sexo,email,telefone,salario_mensal):
    nome = str(nome)
    data_nascimento = str(data_nascimento)
    email = str(email)
    telefone = int(telefone)
    sexo = str(sexo)
    salario_mensal = float(salario_mensal)

    if sexo == 'M':
        print(f"O funcionario {nome} foi cadastrado com sucesso!")
    elif sexo == 'F':
        print(f"A funcionaria {nome} foi cadastrada com sucesso!")
        
    print(f"Nome : {nome}")
    print(f"Nascimento : {data_nascimento}")
    print(f"Emai : {email}")
    print(f"telefone : {telefone}")
    print(f"sexo : {sexo}")
    print(f"Salario mensal : {salario_mensal}")

def comissao(salario_mensal,vendas):
    salario_mensal = float(salario_mensal)
    vendas = int(vendas)
    valor_por_venda = 1000
    
    salario_total = salario_mensal + (vendas * valor_por_venda)

    print(f"O salario total do funcionario é de : {salario_total}") 
