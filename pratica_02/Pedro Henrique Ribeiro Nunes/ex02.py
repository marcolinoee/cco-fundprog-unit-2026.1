idade = int(input('Qual a sua idade? '))
if idade >= 18 and idade < 60:
    print('Você é maior de idade.')
elif idade < 18 and idade > 0:
    print('Você é menor de idade.')
elif idade >= 60 and idade <= 120:
    print('Você é idoso.')
else:
    print('Idade inválida')
