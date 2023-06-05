import funcionarios

nome = input("Digite o Nome do(a) funcionario(a): ")
email = input("Digite o email do(a) funcionario(a): ")
data_nascimento = input("Digite a data do nascimento do(a) funcionario(a): ")
telefone = input("Digite o telefone do(a) funcionario(a): ")
sexo = input("Informe o sexo do funcionario: ")
salario = input("Informe o salário mensal do funcionario: R$ ")

funcionarios.cadastrar(nome,data_nascimento,sexo,email,telefone,salario_mensal=salario)
vendas = input("Informe a quantidade de vendas do(a) funcionario(a): ")
funcionarios.comissao(salario_mensal=salario,vendas=vendas)