sal = float(input("Insira o valor do salário: R$ "))
if sal < 1500:
              percentual = 0.15
elif sal >= 1500 and sal < 3000:
            percentual = 0.10
else:  
            percentual = 0.05
aumento = sal * percentual
novo_sal = sal + aumento
print("Valor do aumento: R$ " + str(aumento))
print("Novo salário: R$ " + str(novo_sal))  