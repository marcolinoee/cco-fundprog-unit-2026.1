lab = [
    ["L", "M", "L","O","O"],
    ["O", "L", "M","L","O"],
    ["M", "O", "O","O","M"],
    ["L", "M", "L","O","O"],
    
]
mapa_lab = 0
for i in range(len(lab)):
    for j in range(len(lab[0])):
        print(lab[i][j], end=' ')
    print()


livre = ocupado = manutencao = 0
for i in range(len(lab)):
    for j in range(len(lab[0])):
        if lab[i][j] == "L":
            livre += 1
        elif lab[i][j] == "O":
            ocupado += 1
        elif lab[i][j] == "M":
            manutencao += 1
            
        
linha = int(input("Digite a linha(0-5): "))
coluna = int(input("Digite a coluna(0-4): "))

if linha < 0 or linha > 5 or coluna < 0 or coluna > 4:
    print("posicao invalida")
elif lab[linha][coluna] == "L":
    print(f"reserva realizada no laboratorio {mapa_lab}")
elif lab[linha][coluna] == "O":
    print("laboratorio ocupado")
elif lab[linha][coluna] == "M":
    print("laboratorio em manutencao")
else:
    print("erro")
    
    print(mapa_lab)

        