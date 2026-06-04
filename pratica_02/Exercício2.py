idade = int(input('Insira sua idade para saber sua faixa etária: '))

if idade < 18:
    print('Você é menor de idade')
if idade >= 18 and idade < 59:
    print('Você é maior de idade')
if idade >= 60:
    print('Você é idoso')