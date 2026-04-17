while True:
    nota = float(input("Insira a nota do aluno: "))
    if nota < 0 or nota > 10:
        print("Nota inválida. Tente novamente.") 
    else:        break
print("Nota válida. O aluno foi aprovado." if nota >= 6 else "Nota válida. O aluno foi reprovado.")  