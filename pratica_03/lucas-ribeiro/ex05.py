def ler_notas():
    n1 = float(input('Digite a nota da 1º unidade: '))
    n2 = float(input('Digite a nota da 2º unidade: '))
    return n1, n2

def calcular_media(n1, n2):
    return (n1+n2)/2

def verificar_situacao(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'
    
def exibir_resultado(nome, media, situacao):
    print(f'Aluno: {nome}\nMédia: {media}\nSituação: {situacao}')

def main():
    nome = str(input('Digite seu nome: '))

    n1, n2 = ler_notas()

    media = calcular_media(n1, n2)

    situacao = verificar_situacao(media)

    exibir_resultado(nome, media, situacao)

main()