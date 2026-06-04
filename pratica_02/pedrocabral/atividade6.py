nota = int(input("insira sua nota  "))
while nota < 0 or nota > 10:
    print("nota invalida")
    nota = int(input("tente novamente: "))
if nota >= 0 and nota <= 10:
    print("nota valida")
else:
    print("erro")
