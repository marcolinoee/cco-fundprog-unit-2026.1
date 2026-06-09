Idade = int(input("Digite sua idade: "))

if Idade < 18:
    print("Você é menor de idade.")
elif Idade >= 18 and Idade < 59:
    print("Você é maior de idade.")
else:
    print("Você é idoso.")