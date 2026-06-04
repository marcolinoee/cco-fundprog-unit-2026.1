# Validação de nota -  Python

nota = float(input("Digite a sua nota: "))
while nota < 0 or nota > 10:
    print("Inválido. O valor deve ser de 0 a 10: ")
    nota = float(input("Digite novamente: "))

if nota >= 0 and nota <= 10:
    print("Nota validada.")