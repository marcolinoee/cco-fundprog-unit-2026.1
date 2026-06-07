def ler_notas():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    return n1, n2
 
def calcular_media(n1, n2):
    return (n1 + n2) / 2
 
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
 
def exibir_relatorio(nome, media, situacao):
    print("\n--- Relatório Final ---")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

nome = input("Nome do aluno: ")
n1, n2 = ler_notas()
media = calcular_media(n1, n2)
situacao = verificar_situacao(media)
exibir_relatorio(nome, media, situacao)