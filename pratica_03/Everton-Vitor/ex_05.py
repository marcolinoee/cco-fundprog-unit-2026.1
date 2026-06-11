def lerNotas():
    name = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    return name, n1, n2


def CalcularMedia(n1, n2):
    return (n1 + n2) / 2

def verificarSituacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0 and media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado"
    
def exibirResultado(name, media, situacao):
    print(f"Aluno: {name}")
    print(f"A média das notas é: {media:.1f}")
    print(f"Situação: {situacao}")

name, n1, n2 = lerNotas()
media = CalcularMedia(n1, n2)
situacao = verificarSituacao(media)
exibirResultado(name, media, situacao)