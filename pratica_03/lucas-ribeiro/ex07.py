def calcular_media(n1, n2):
    return (n1+n2)/2

def verificar_situacao(media):
    if media >= 7:
       return "Aprovado"  
    else:
       return "Reprovado"

n1 = 8
n2 = 6
media = calcular_media(n1, n2)
situacao = verificar_situacao(media)

print(media)
print(situacao)


