'''

n1 = 8
n2 = 6
media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

'''

def calcularMedia():
    n1 = 8
    n2 = 6
    media = (n1 + n2) / 2
    return media


def verificarSituacao(media):
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

media = calcularMedia()
verificarSituacao(media)