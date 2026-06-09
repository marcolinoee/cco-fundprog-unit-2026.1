# Calculadora de Freelancer - Python

valorHora = float(input("Digite o valor cobrado por hora:  "))
horasEstimadas = float(input("Digite a estimativa de horas para conclusão: "))

valorBruto = valorHora * horasEstimadas
impostos = valorBruto * 0.15
valorLiquido = valorBruto - impostos

print("ORÇAMENTO DO PROJETO:")
print(f"Valor bruto: R$ {valorBruto}")
print(f"Impostos (15%): R$ {impostos}")
print(f"Valor líquido: R$ {valorLiquido}")