sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

while True:
    linha = int(input("Digite a linha (-1 para sair): "))
    if linha == -1:
        break
    coluna = int(input("Digite a coluna: "))

    if linha < 0 or linha >= len(sala) or coluna < 0 or coluna >= len(sala[0]):
        print("Posição fora dos limites.")
    elif sala[linha][coluna] == "L":
        sala[linha][coluna] = "O"
        print("Reserva realizada.")
    else:
        print("Assento indisponível.")

    for l in sala:
        print(l)