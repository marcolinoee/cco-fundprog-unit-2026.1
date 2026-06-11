def calcular_media(n1, n2):
    return (n1+n2)/2

n1 = float(input('Digite a nota da 1º unidade: '))
n2 = float(input('Digite a nota da 2º unidade: '))

print(f'A média das notas da 1º unidade: {n1:.1f} e 2º unidade: {n2:.1f}.\nMédia: {calcular_media(n1, n2):.1f}')