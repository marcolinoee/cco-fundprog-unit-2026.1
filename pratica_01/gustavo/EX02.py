valor_hora = float(input("Digite o valor cobrado por hora: R$ "))
horas = float(input("Digite a estimativa de horas para conclusão: "))

valor_bruto = horas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print("=== RESUMO DO PROJETO ===")
print("Valor bruto:   R$ ".format() + str(valor_bruto))
print("Impostos (15%): R$ " + str(impostos))
print("Valor líquido: R$ " + str(valor_liquido))