from ex03 import calcular_media, n1, n2

def verificar_situacao(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'
    
print(f'Situação: {verificar_situacao(calcular_media(n1, n2))}')

