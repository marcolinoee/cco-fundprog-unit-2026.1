salario = float(input('Digite o salário para reajuste: R$'))
if salario <= 1.500:
    aumento = salario * 0.15
    print (f'O salário reajustado ficou de: R${salario + aumento:.3f}')
elif salario > 1.500 and salario <= 3.000:
    aumento = salario * 0.10
    print (f'O salário reajustado ficou de: R${salario + aumento:.3f}')
else:
    aumento = salario * 0.05
    print (f'O salário reajustado ficou de: R${salario + aumento:.3f}')
