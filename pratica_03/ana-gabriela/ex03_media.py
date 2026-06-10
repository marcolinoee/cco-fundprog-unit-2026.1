def calcular_media(n1, n2):
    return (n1 + n2) / 2
 
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = calcular_media(n1, n2)
print(f"Média: {media:.1f}")
 