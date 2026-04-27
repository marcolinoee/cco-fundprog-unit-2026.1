usuario = input("Digite seu nome: ")
dataDeNascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
altura = float(input("Digite sua altura (em metros): "))

def calcularIdade(dataDeNascimento):
    from datetime import datetime
    hoje = datetime.now()
    nascimento = datetime.strptime(dataDeNascimento, "%d/%m/%Y")
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

idade = calcularIdade(dataDeNascimento)

print(f"Olá, {usuario}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.")