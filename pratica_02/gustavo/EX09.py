salario = float(input("Digite o salário atual: R$ "))

if salario <= 1500:
    percentual = 0.15
elif salario <= 3000:
    percentual = 0.10
else:
    percentual = 0.05

reajuste = salario * percentual
novo_salario = salario + reajuste

print("Salário atual:  R$ {}".format(salario))
print("Reajuste ({}%): R$ {}".format(int(percentual * 100), reajuste))
print("Novo salário:   R$ {}".format(novo_salario))