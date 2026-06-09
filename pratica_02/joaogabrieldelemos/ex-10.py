opcao = -1
print ('-' * 40)
print ('Menu de opções')
print ('1 - Somar')
print ('2 - Subtrair')
print ('0 - Sair')
print ('-' * 40)
while opcao not in [1, 2, 0]:
    opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    resultado = num1 + num2
    print(f'O resultado da soma é: {resultado}')
elif opcao == 2:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    resultado = num1 - num2
    print(f'O resultado da subtração é: {resultado}')
elif opcao == 0:
    print('Encerrando o programa. Até mais!')
else:
    print('Opção inválida. Por favor, escolha uma opção válida.')
