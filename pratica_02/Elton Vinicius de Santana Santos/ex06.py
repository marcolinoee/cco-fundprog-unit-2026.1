def ler_Nota():
    nota = float(input("Digite uma nota entre 0 e 10: "))
    while nota < 0 or nota > 10:
        print("Nota inválida. Tente novamente.")
        nota = float(input("Digite uma nota entre 0 e 10: "))
    return nota

nota = ler_Nota()