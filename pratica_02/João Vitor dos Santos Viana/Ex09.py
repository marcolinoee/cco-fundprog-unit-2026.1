salario = float(input("Digite o salário do funcionário: "))

if salario > 1500 and salario <= 3000:
    aumento = salario * 0.10
elif salario <= 1500:
    aumento = salario * 0.15
else:
    aumento = salario * 0.05

print("Aumento:", aumento)
print("Novo salário:", salario + aumento)