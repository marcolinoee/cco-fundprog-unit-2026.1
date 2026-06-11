print("="*50)
print("programa que simule o registro de um novo usuário")
print("="*50)
Nome = input("Qual Seu Nome: ")
Ano_Nascimento = int(input("Digite o Ano de Nascimento: "))
Altura = float(input("Qual Sua Altura: "))
Ano_Atual = 2026
Idade = Ano_Atual - Ano_Nascimento

print(f"Olá, {Nome}! Você tem {Idade} anos e sua altura é de {Altura}m. Registro concluído.")