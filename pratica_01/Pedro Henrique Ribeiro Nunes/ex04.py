idade = int(input('Qual a sua idade? '))
exp = int(input('Quantos anos de experiência você tem? '))

while idade >= 18 and exp > 2: 
    print('Acesso liberado.')
    break
while idade < 18 and exp <= 2:
    print('Acesso negado.')
    break
