#Refatorando o ex06 (Valiadação de nota)
for i in range (999):
    nota = float(input("insira a nota do aluno (0 a 10):"))
    if nota >=0 and nota <= 10:
        if nota >= 6:
            print("Nota inválida. O aluno foi aprovado.")
        else:
            print("Nota válida. O aluno foi reprovado.") 
    else:
        print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")

#Com o 'for', o código fica mais seguro contra loops infinitos reais, pois há um limite definido no range.

