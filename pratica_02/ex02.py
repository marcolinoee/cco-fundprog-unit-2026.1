id = int(input("Digite a sua idade: "))
if id < 18:
    print("Você é menor de idade.")
elif id >= 18 and id <60:
    print("Você é maior de idade. ")
else:
    print("Você é um idoso. ")