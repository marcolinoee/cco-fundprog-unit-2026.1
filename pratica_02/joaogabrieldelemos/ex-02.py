idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 120:
    print ('Idade inválida.')
    idade = int(input('Digite uma idade válida: '))
if idade < 18:
    print ('Menor de idade')
elif idade < 60:
    print ('Maior de idade')
else:
    print ('Idoso')