valor_cobrado_hora = int(input('Digite o valor cobrado por hora: '))
estimativa_conclusao_horas = int(input('Digite a estimativa de horas para conclusão completa: '))

valor_bruto = valor_cobrado_hora * estimativa_conclusao_horas
valor_impostos = (valor_bruto / 100) * 15
valor_liquido = valor_bruto - valor_impostos

print(f"valor bruto: {valor_bruto}")
print(f"valor impostos: {valor_impostos}")
print(f"valor liquido: {valor_liquido}")