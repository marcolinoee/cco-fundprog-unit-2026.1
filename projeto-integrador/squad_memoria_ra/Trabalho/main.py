import os
from funçoes import limpa, motor_simples_nacional, motor_lucro_presumido, lucro_real, voltar_menu, motor_lucro_real


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
        presumido = motor_lucro_presumido(faturamento, ramo)
        real = motor_lucro_real(faturamento, folha_de_pagamento, custos_operacionais)

        if faturamento > 4800000:
            print("\033[1;33m⚠ Atenção: faturamento acima de R$ 4.800.000. Empresa não pode optar pelo Simples Nacional.\033[m\n")
            simples = None

        print("=" * 44)
        if simples is None and real is None:
            print("Regime disponível: apenas Lucro Presumido.")
            lucro_real(faturamento, presumido, folha_de_pagamento, custos_operacionais)
        elif simples is None and presumido is None:
            print("Regime disponível: apenas Lucro Real.")
            lucro_real(faturamento, presumido, folha_de_pagamento, custos_operacionais)
        elif real is None and presumido is None:
            print("Regime disponível: apenas Simples Nacional.")
            lucro_real(faturamento, presumido, folha_de_pagamento, custos_operacionais)
        elif simples is None and real is not None and presumido is not None:
            if presumido < real:
                print(f"Lucro Presumido é mais barato. Economia de:\033[1;32m R$ {real - presumido:,.2f} \033[m")
                lucro_real(faturamento, presumido, folha_de_pagamento, custos_operacionais)
            elif real < presumido:
                print(f"Lucro Real é mais barato. Economia de:\033[1;32m R$ {presumido - real:,.2f} \033[m")
                lucro_real(faturamento, real, folha_de_pagamento, custos_operacionais)
            else:
                print("Lucro Presumido e Lucro Real têm o mesmo custo.")
                lucro_real(faturamento, presumido, folha_de_pagamento, custos_operacionais)
        elif real is None and simples is not None and presumido is not None:
            if presumido < simples:
                print(f"Lucro Presumido é mais barato. Economia de:\033[1;32m R$ {simples - presumido:,.2f} \033[m")
                lucro_real(faturamento, presumido, folha_de_pagamento, custos_operacionais)
            elif simples < presumido:
                print(f"Simples Nacional é mais barato. Economia de:\033[1;32m R$ {presumido - simples:,.2f} \033[m")
                lucro_real(faturamento, simples, folha_de_pagamento, custos_operacionais)
            else:
                print("Lucro Presumido e Simples Nacional têm o mesmo custo.")
                lucro_real(faturamento, presumido, folha_de_pagamento, custos_operacionais)
        elif presumido is None and real is not None and simples is not None:
            if simples < real:
                print(f"Simples Nacional é mais barato. Economia de:\033[1;32m R$ {real - simples:,.2f} \033[m")
                lucro_real(faturamento, simples, folha_de_pagamento, custos_operacionais)
            elif real < simples:
                print(f"Lucro Real é mais barato. Economia de:\033[1;32m R$ {simples - real:,.2f} \033[m")
                lucro_real(faturamento, real, folha_de_pagamento, custos_operacionais)
            else:
                print("Simples Nacional e Lucro Real têm o mesmo custo.")
                lucro_real(faturamento, simples, folha_de_pagamento, custos_operacionais)
        elif real is not None and presumido is not None and simples is not None:
            if simples < presumido and simples < real:
                print(f"Simples Nacional é mais barato. Economia de:\033[1;32m R$ {presumido + real - simples:,.2f} \033[m")
                lucro_real(faturamento, simples, folha_de_pagamento, custos_operacionais)
            elif presumido < simples and presumido < real:
                print(f"Lucro Presumido é mais barato. Economia de:\033[1;32m R$ {simples + real - presumido:,.2f} \033[m")
                lucro_real(faturamento, presumido, folha_de_pagamento, custos_operacionais)
            elif real < presumido and real < simples:
                print(f"Lucro Real é mais barato. Economia de:\033[1;32m R$ {simples + presumido - real:,.2f} \033[m")
                lucro_real(faturamento, real, folha_de_pagamento, custos_operacionais)
            else:
                print("Os três têm o mesmo custo.")
                lucro_real(faturamento, simples, folha_de_pagamento, custos_operacionais)

        voltar_menu()

    except ValueError:
        limpa()
        print('Dados inválidos! Digite apenas números.')
        input("Pressione Enter para tentar novamente...")