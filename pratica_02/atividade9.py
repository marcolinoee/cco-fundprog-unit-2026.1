salario = int(input("qual o valor do seu salario?  "))
if salario <= 1500:
    reajuste = salario * 0.15
    salario_reajustado = salario + reajuste
    print(f"o valor do seu salario reajustado é: R${salario_reajustado:.2f}")
elif salario > 1500 and salario <= 3000:
    reajuste = salario * 0.10
    salario_reajustado = salario + reajuste
    print(f"o valor do seu salario reajustado é: R${salario_reajustado:.2f}")
elif salario > 3000:
    reajuste = salario * 0.05
    salario_reajustado = salario + reajuste
    print(f"o valor do seu salario reajustado é: R${salario_reajustado:.2f}")    