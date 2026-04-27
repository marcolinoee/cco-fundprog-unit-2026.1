valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

def calcular_salario_bruto(valor_hora, horas_trabalhadas):
    return valor_hora * horas_trabalhadas

def calcular_desconto_inss(valor_bruto):
    return valor_bruto * 0.15

def calcular_valor_liquido(valor_bruto, desconto_inss):
    return valor_bruto - desconto_inss

print(f"Valor bruto: R${calcular_salario_bruto(valor_hora, horas_trabalhadas):.2f}")
print(f"Desconto INSS: R${calcular_desconto_inss(calcular_salario_bruto(valor_hora, horas_trabalhadas)):.2f}")
print(f"Valor líquido: R${calcular_valor_liquido(calcular_salario_bruto(valor_hora, horas_trabalhadas), calcular_desconto_inss(calcular_salario_bruto(valor_hora, horas_trabalhadas))):.2f}")