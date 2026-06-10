valor_cobrado = float(input('Quanto você conbra por hora? '))
est_hora = float(input('Em quanto tempo tempo você conclui seu trabalho? '))

valor_bruto = valor_cobrado * est_hora
imposto = valor_bruto * 0.15
valor_liq = valor_bruto - imposto

print(f'Valor bruto= R$ {valor_bruto}, impostos= {imposto} e o valor líquido= {valor_liq}')