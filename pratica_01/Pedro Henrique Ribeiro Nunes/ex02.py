valor = float(input('Qual o valor cobrado por hora? '))
horas = float(input('Qual a estimativa de horas para conclusão? '))
bruto = horas * valor
impostos = valor * 0.15
liquido = bruto - impostos
print(f'Valor Bruto: {bruto}\nValor de impostos: {impostos}\nValor Líquido: {liquido}')
