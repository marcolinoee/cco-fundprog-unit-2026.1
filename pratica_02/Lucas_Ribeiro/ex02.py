idade = int(input('Informe sua idade: '))

if idade >= 18 and  idade <= 59:
    print(f'Você tem {idade} anos, portanto é maior de idade!')
elif idade >= 60:
    print(f'Você tem {idade} anos, portanto é idoso!')
else: 
    print(f'Você tem {idade} anos, portanto é menor de idade!')