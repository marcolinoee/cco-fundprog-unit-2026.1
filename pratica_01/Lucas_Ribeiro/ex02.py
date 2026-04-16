valor_hora = float(input('Digite o valor cobrado por hora: '))
estimativa_hora = float(input('Informe a estimativa de horas para conclusão: '))

valor_bruto = estimativa_hora * valor_hora
imposto = valor_bruto * 0.15
valor_liquido = valor_bruto - imposto

print(f'''
        Valor Bruto: R$ {valor_bruto:.2f}
        Impostos: R$ {imposto:.2f}
        Valor líquido total: R$ {valor_liquido:.2f}

    ''')