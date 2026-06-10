salario = float(input('Insira seu salário: '))

if salario == 1500.00:
    salario = salario + (salario * 0.15)
    print(f'Após um aumento de 15%, seu salário agora é de: {salario:.2f}R$')
elif salario > 1500.00 and 3000.00:
    salario = salario + (salario * 0.10)
    print(f'Após um aumento de 10%, seu salário agora é de: {salario:.2f}R$')
elif salario > 3000.00:
    salario = salario + (salario * 0.05)
    print(f'Após um aumento de 5%, seu salário agora é de: {salario:.2f}R$')
else:
    print('O valor não é elegível para cálculo')