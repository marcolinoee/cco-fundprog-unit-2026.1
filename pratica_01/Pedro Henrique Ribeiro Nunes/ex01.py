user = str(input('Informe seu nome de usuário: '))
nascimento = int(input('Informe o ano em que você nasceu: '))
altura = float(input('Informe sua altura, em metros: '))

idade = 2026 - nascimento
print(f'Olá, {user}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.')