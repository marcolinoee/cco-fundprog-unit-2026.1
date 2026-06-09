nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido!")
    nota = float(input("Por favor, digite uma nota válida (entre 0 e 10): "))

print(f"Sucesso! Você digitou a nota: {nota}")