from datetime import datetime

def obter_nome_sobrenome():
    nome = input("Qual é o seu nome? ")
    sobrenome = input("Qual é o seu sobrenome? ")
    return nome, sobrenome

def obter_data_nascimento():
    data_str = input("Qual é a sua data de nascimento (formato: DD/MM/AAAA)? ")
    data = datetime.strptime(data_str, "%d/%m/%Y")
    return data

def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    diferenca = data_atual - data_nascimento
    idade = diferenca.days // 365
    return idade

nome, sobrenome = obter_nome_sobrenome()
data_nascimento = obter_data_nascimento()
idade = calcular_idade(data_nascimento)

# print({datetime.now()})

print(f"Olá, {nome} {sobrenome}!")
print(f"Você tem {idade} anos de idade.")