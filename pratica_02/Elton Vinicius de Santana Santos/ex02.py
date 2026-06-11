print("="*50)
print("------------Classificaçã0-de-Idade----------------")
print("="*50)

Idade = int(input("Qual sua Idade: "))
if 18 <= Idade <= 59:
    print("Maior de Idade")
elif Idade >= 60:
    print("Idoso")
else:
    print("Menor de Idade")