idade = int(input('Informe sue idade: '))
exp_ano = int(input('Digite quantos anos de experiência você possui: '))

acesso = (idade >= 18) and (exp_ano > 2)

print(f'Chave de acesso: {acesso}')