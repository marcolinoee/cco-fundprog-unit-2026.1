
print("="*50)
print("script para calcular o valor de um projeto freelancer")
print("="*50)

valor_hora = float(input("Digite o seu valor por hora (R$): "))
horas_estimadas = float(input("Digite a estimativa de horas para o projeto: "))

valor_bruto = valor_hora * horas_estimadas
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print("="*50)
print(f"💰 Valor Bruto: R$ {valor_bruto:.2f}")
print(f"💸 Impostos (15%): R$ {impostos:.2f}")
print(f"✅ Valor Líquido: R$ {valor_liquido:.2f}")
print("="*50)