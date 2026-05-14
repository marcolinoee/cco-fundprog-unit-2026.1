print('---Digite uma das opções abaixou---')

while True:
    print('1- Somar')
    print('2- Subtrair')
    print('3- Sair')

    opcao = input('Escolha uma opção:')

    if opcao == '0':
        print('Encerrando o progama...')
        break

    elif opcao =='1':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print(f'O resultado da soma foi: {n1 + n2}')

    elif opcao =='2':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print(f'O resultado da subtração foi: {n1 - n2}')
    else:
        print('Opção inválida! Tente novamente.')