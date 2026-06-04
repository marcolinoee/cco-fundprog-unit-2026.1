from os import system as s

salario = float(input('informe seu salário: '))
salario_reajuste = 0
if salario >= 1500.01 and salario <= 3000:
    salario_reajuste += (salario + (salario * 0.1))
    s('cls')
    print(f'Seu salário de R${salario:.2f} sofreu um aumento de 10%!\n\nResultando no seu novo salário de R${salario_reajuste:.2f}')
elif salario > 3000:
    salario_reajuste += (salario + (salario * 0.05))
    s('cls')
    print(f'Seu salário de R${salario:.2f} sofreu um aumento de 5%!\n\nResultando no seu novo salário de R${salario_reajuste:.2f}')
else:
    salario_reajuste += (salario + (salario * 0.15))
    s('cls')
    print(f'Seu salário de R${salario:.2f} sofreu um aumento de 15%!\n\nResultando no seu novo salário de R${salario_reajuste:.2f}')