salário = float(input("Digite o salário: "))
aumento = 0

if salário < 1500:
    aumento = salário * 0.15
elif salário <= 3000:
    aumento = salário * 0.1
else:
    aumento = salário * 0.05

salário += aumento
print(f"Salário com aumento: {salário}")
