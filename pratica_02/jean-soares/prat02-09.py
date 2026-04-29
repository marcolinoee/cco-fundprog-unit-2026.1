# Reajuste de Salário - Python

salario = float(input("Digite o seu salário atual: "))

if salario > 0 and salario <= 1500:
    reajuste = salario + salario * 0.15
    print(f"Seu novo salário reajustado é de: R${reajuste}")

elif salario > 1500 and salario <= 3000:
    reajuste = salario + salario * 0.10
    print(f"Seu novo salário reajustado é de: R${reajuste}")

else:
    reajuste = salario + salario * 0.05
    print(f"Seu novo salário reajustado é de: R${reajuste}")