nome = str(input('Informe seu nome: '))
ano_nascimento = int(input('Digite o ano que você nasceu: '))
altura = float(input('Informe sua altura: '))

ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f'Olá {nome}, você nasceu no ano de {ano_nascimento}, portanto possui {idade} anos e {altura}m de altura!')