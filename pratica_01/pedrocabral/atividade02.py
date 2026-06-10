
horas_trabalhadas = int(input("quantas horas voce trabalhou?  "))
valor_hora = float(input("qual o valor da sua hora de trabalho?  "))
valor_bruto = horas_trabalhadas * valor_hora
print(f"o valor bruto do seu salario é: R${valor_bruto:.2f}")
imposto = valor_bruto * 0.11
print(f"o valor do imposto a ser pago é: R${imposto:.2f}")
liquido = valor_bruto - imposto
print(f"o valor liquido do seu salario é: R${liquido:.2f}")