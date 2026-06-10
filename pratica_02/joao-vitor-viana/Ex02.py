idade = int(input('Quantos anos você tem? '))

if idade < 18:
    print('Menor de idade')
elif idade > 18 and idade <= 59:
    print('Maior de idade')
else:
    print('Idoso')