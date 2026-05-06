idade= int(input("Digite a idade: "))
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 59:
    print("Você é maior de idade.")
else:
    print("Você é idoso.")
