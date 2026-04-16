reajuste = ''
salario = float(input('Informe seu salário: '))
if(salario <= 1500):
    reajuste = salario + ((salario / 100) * 15)
    print(f'Novo salario com 15% de aumento: {reajuste}')
elif(salario > 1500 and salario <= 3000):
    reajuste = salario + ((salario / 100) * 10)
    print(f'Novo salario com 10% de aumento: {reajuste}')
else:
    reajuste = salario + ((salario / 100) * 5)
    print(f'Novo salario com 5% de aumento: {reajuste}')