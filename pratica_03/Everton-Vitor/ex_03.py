def CalcularMedia(n1, n2):
    return (n1 + n2) / 2

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = CalcularMedia(n1, n2)
print(f"A média das notas é: {media:.1f}")