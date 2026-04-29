mnota = 0.0
for i in range (5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    if nota > mnota:
        mnota = nota
        print("=" * 30)
        print(f"A maior nota é: {mnota}.")