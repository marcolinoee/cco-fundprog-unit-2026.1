# Refatoração de while para for - Python

for tentativas in range(10):
    nota = float(input("Digite a sua nota: "))
    
    if nota >= 0 and nota <= 10:
        print("Nota validada.")
        break
    else:
        print("Inválido. O valor deve ser de 0 a 10: ")
else:
    print("Limite excedido!")