salario_atual = float(input('Quanto você ganha por mês? '))

if salario_atual <= 1500:
    aumento = salario_atual * (15 / 100)
elif salario_atual <= 3000:
    aumento = salario_atual * (10 / 100)
else:
    aumento = salario_atual * (5 / 100)

salario_novo = salario_atual + aumento

print(f'Seu salario com reajustes ficou R$ {salario_novo} e teve um aumento de R$ {aumento}.')