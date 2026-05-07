import os

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_menu():
    print("="*44)
    print("[1] Nova simulação")
    print("[2] Sair do programa")
    print('(Não escreva por extenso)')
    print("="*44)

    escolha = input("Digite sua escolha: ")
    while True:
        if escolha == '1':
            break
        elif escolha == '2':
            print('Encerrando Programa.....')
            exit()
        while escolha != '1' and escolha != '2' or escolha == '':
                limpa()
                print('Escolha um valor válido (1 ou 2) e não escreva por extenso: ')
                escolha = input('Digite novamente: ')

def motor_lucro_real(faturamento, folha_de_pagamento, custos_operacionais) -> float | None:
    lucro_liquido = faturamento - folha_de_pagamento - custos_operacionais
    if lucro_liquido > 0:
        imposto_base = lucro_liquido * 0.24
        calculo_adicional = (lucro_liquido - 240000) * 0.10
        if calculo_adicional > 0:
            adicional = calculo_adicional
        else:
            adicional = 0.0
    else:
        imposto_base = 0.0
        adicional = 0.0 
    calculo_pis_cofins = (faturamento * 0.0925) - (custos_operacionais * 0.0925)
    if calculo_pis_cofins > 0:
        pis_cofins = calculo_pis_cofins
    else:
        pis_cofins = 0.0
    imposto = imposto_base + adicional + pis_cofins
    print("--- Lucro Real ---")
    print(f"Total imposto: \033[1;31mR$ {imposto:,.2f}\033[m\n")
    return imposto


def lucro_real(faturamento, imposto, folha_de_pagamento, custos_operacionais):
    lucro = faturamento - imposto - folha_de_pagamento - custos_operacionais
    if lucro < 0:
        print("A empresa teve prejuízo no ano!")
        print(f"Está devendo: \033[1;31m R$ {abs(lucro):,.2f} \033[m")
    else:
        print(f"Lucro após impostos: \033[1;34mR$ {lucro:,.2f}\033[m")

def motor_simples_nacional(faturamento: float, ramo: str) -> float | None:
    if ramo == "Comércio":
        if faturamento <= 180000: aliquota = 0.04
        elif faturamento <= 360000 and faturamento > 180000: aliquota = 0.073
        elif faturamento <= 720000 and faturamento > 360000: aliquota = 0.095
        elif faturamento <= 1800000 and faturamento > 720000: aliquota = 0.107
        else: aliquota = 0.143
    elif ramo == "Serviços":
        if faturamento <= 180000: aliquota = 0.06
        elif faturamento <= 360000 and faturamento > 180000: aliquota = 0.112
        elif faturamento <= 720000 and faturamento > 360000: aliquota = 0.135
        elif faturamento <= 1800000 and faturamento > 720000: aliquota = 0.16
        else: aliquota = 0.21
    elif ramo == "Indústrias":
        if faturamento <= 180000: aliquota = 0.045
        elif faturamento <= 360000 and faturamento > 180000: aliquota = 0.078
        elif faturamento <= 720000 and faturamento > 360000: aliquota = 0.10
        elif faturamento <= 1800000 and faturamento > 720000: aliquota = 0.113
        else: aliquota = 0.147
    else: return None

    imposto = faturamento * aliquota
    print("--- Simples Nacional ---")
    print(f"Total imposto: \033[1;31mR$ {imposto:,.2f}\033[m\n")
    return imposto

def motor_lucro_presumido(faturamento, ramo):
    if ramo == "Comércio" or ramo == "Indústrias":
        base = faturamento * 0.08
    elif ramo == "Serviços":
        base = faturamento * 0.32
    else: return None

    irpj, csll, pis, cofins = base * 0.15, base * 0.09, faturamento * 0.0065, faturamento * 0.03
    imposto = irpj + csll + pis + cofins
    print("--- Lucro Presumido ---")
    print(f"Total imposto: \033[1;31mR$ {imposto:,.2f}\033[m\n")
    return imposto