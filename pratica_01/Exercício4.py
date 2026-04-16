idade = int(input('Insira a idade: '))
exp = int(input('Insira o tempo de experiência em anos: '))

acesso = (idade >= 18) and (exp >= 2)
print('Acesso concedido')