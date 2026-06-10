sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

L = 0
O = 0

for i in range(len(sala)):
    for j in range(len(sala[0])):
        if sala[i][j] == "L":
            L += 1
        else:
            O += 1
            

linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))

if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
    print("assento invalido")
    
elif sala[linha][coluna] == "L":
    print("reserva realizada")
else:
    print("assento ocupado")
    

