seuSalario = float(input("Digite o seu salário: "))
if seuSalario <= 1500:
    aumento = seuSalario * 0.15
    print(f"O valor do aumento é: {aumento}")
elif seuSalario > 1501 and seuSalario <= 3000:
    aumento = seuSalario * 0.10
    print(f"seu salario é {seuSalario}, o valor do aumento é: {aumento} no total seu salario é: {seuSalario + aumento}")
else:
    aumento = seuSalario * 0.05
    print(f"seu salario é {seuSalario}, o valor do aumento é: {aumento} no total seu salario é: {seuSalario + aumento}")