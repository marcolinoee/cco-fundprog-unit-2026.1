def calcular_media(n1, n2):
    return (n1 + n2) / 2
 
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = calcular_media(n1, n2)
print(f"Média: {media:.1f}")
 
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
 
media = calcular_media(n1, n2)
situacao = verificar_situacao(media)
print(f"Situação: {situacao}")
 