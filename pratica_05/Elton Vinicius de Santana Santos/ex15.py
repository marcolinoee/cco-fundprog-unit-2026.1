sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))

if 0 <= linha < len(sala) and 0 <= coluna < len(sala[0]):
    if sala[linha][coluna] == "L":
        sala[linha][coluna] = "O"
        print("Reserva realizada")
    else:
        print("Assento indisponível")
else:
    print("Posição inválida")

for linha in sala:
    print(linha)