num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número:'))
result = ''
while True:
    print('''1-Somar
2-Subtrair
0-Sair''')
    opcao = str(input('Digite uma opção: '))
    if opcao == '1':
        result = num1 + num2
        print(f'A soma foi igual a {result}')
        continue
    elif opcao == '2':
        result = num1 - num2
        print(f'A subtração foi igual a {result}')
        continue
    elif opcao == '0':
        print('Adeus.')
        break