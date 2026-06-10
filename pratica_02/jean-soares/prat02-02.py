# Faixa etária essencial - Python

idade = int(input("Digite a idade do usuário: "))
if idade > 0 and idade < 18 :
    print("O usuário é menor de idade.")

elif idade >= 18 and idade <= 59:
    print("O usuário é maior de idade.")

elif idade >= 60 and idade <= 120:
    print("O usuário é idoso.")

else:
    print("Idade inválida!")