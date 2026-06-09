idade = int(input('Informe sua idade: '))
anos_exp = int(input('Digite quantos anos de experiência você tem? '))

acesso = (idade >= 18) and (anos_exp > 2)

print(f'Chave de acesso: {acesso}')