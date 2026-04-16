print('Bem vindo! insira as informações pedidas abaixo.')

nome = str(input('\nInsira seu nome: '))
ano = int(input('Insira seu ano de nascimento: '))
altura = float(input('Insira sua altura em metros: '))

idade = (2026 - ano)

print(f"\nOlá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.")