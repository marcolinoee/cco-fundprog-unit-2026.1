import os
from funcoes2 import *


while True:
    limpa()
    print('''Olá, seja bem-vindo ao Simulador de Planejamento e Elisão Tributária do grupo Memória Rã.
Forneça os dados solicitados abaixo para continuar.''')

    try:
        faturamento = float(input('Valor do Faturamento 12m: '))
        while faturamento <= 0:
            limpa()
            faturamento = float(input('O faturamento deve ser positivo. Digite novamente: '))

        folha_de_pagamento = float(input('Valor da Folha de Pagamento: '))
        while folha_de_pagamento < 0 or folha_de_pagamento > faturamento:
            limpa()
            print('A folha deve ser positiva e não pode ser maior que o faturamento.')
            folha_de_pagamento = float(input('Digite novamente a folha: '))

        custos_operacionais = float(input('Valor dos custos operacionais: '))
        while custos_operacionais < 0:
            limpa()
            print('Custos operacionais não podem ser negativos.')
            custos_operacionais = float(input('Digite novamente os custos: '))
        limpa()
        print('''\nSelecione o ramo de atividade:
[1] Comércio
[2] Serviços
[3] Indústrias
(Não escreva por extenso)''')

        opcao = input('Digite o número do ramo: ')
        while opcao != '1' and opcao != '2' and opcao != '3' or opcao == '':
            limpa()
            opcao = input('Opção inválida! Digite 1, 2 ou 3 (Não escreva por extenso): ')

        if opcao == '1':
            ramo = 'Comércio'
        elif opcao == '2':
            ramo = 'Serviços'
        elif opcao == '3':
            ramo = 'Indústrias'

        limpa()
        print(f'Ramo selecionado: \033[1;34m{ramo}\033[m\n')

        simples = motor_simples_nacional(faturamento, ramo)
        presumido = motor_presumido(faturamento, ramo).calcular_imposto()
        real = MotorLucroReal(faturamento, folha_de_pagamento, custos_operacionais).calcular_real()

        if faturamento > 4800000:
            print("\033[1;33m⚠ Atenção: faturamento acima de R$ 4.800.000. Empresa não pode optar pelo Simples Nacional.\033[m\n")

        print("=" * 44)
        comparacao = maior_menor(simples, presumido, real)
        relatorio(comparacao)

        voltar_menu()

    except ValueError:
        limpa()
        print('Dados inválidos! Digite apenas números.')
        input("Pressione Enter para tentar novamente...")