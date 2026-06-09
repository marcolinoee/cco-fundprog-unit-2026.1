def pedir_nota(mensagem):
    while True:
        nota = float(input(mensagem))
        if nota >= 0 and nota <= 10:
            break
        print("Nota inválida! Digite entre 0 e 10.")
    return nota

num1 = pedir_nota("Digite a primeira nota: ")
num2 = pedir_nota("Digite a segunda nota: ")
num3 = pedir_nota("Digite a terceira nota: ")

resultado = (num1 + num2 + num3) / 3

if resultado >= 7:
    print("APROVADO")
else:
    print("REPROVADO")

print(f"Sua média é: {resultado:.2f}")