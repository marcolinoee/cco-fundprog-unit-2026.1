valor = float(input("Insira o valor da hora cobrada: "))
hora = float(input("Insira a quantidade de horas trabalhadas: "))
bruto = valor * hora
imposto = bruto * 0.15
liquido = bruto - imposto
print("Valor bruto: R$ " + str(bruto))
print("Imposto: R$ " + str(imposto))
print("Valor líquido: R$ " + str(liquido))