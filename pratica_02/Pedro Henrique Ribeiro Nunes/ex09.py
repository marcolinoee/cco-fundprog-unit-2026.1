sal = float(input('Informe seu salário: '))
if sal <= 1500:
    novosal = sal * 1.15
elif sal > 1500 and sal <= 3000:
    novosal = sal * 1.1
else:
    novosal = sal * 1.05
print(f'Seu novo salário será: R${novosal:.2f}')
