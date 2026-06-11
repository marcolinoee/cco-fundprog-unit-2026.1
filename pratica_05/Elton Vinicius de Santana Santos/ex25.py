laboratorio = [
    ["L", "O", "L", "M", "L"],
    ["O", "L", "L", "L", "M"],
    ["L", "O", "M", "L", "L"],
    ["L", "L", "O", "L", "L"]
]

print("MAPA DO LABORATÓRIO")

for linha in laboratorio:
    print(linha)

livres = 0
ocupados = 0
manutencao = 0

for linha in laboratorio:
    for computador in linha:
        if computador == "L":
            livres += 1
        elif computador == "O":
            ocupados += 1
        else:
            manutencao += 1

print("Livres:", livres)
print("Ocupados:", ocupados)
print("Manutenção:", manutencao)

linha = int(input("Digite a fileira: "))
coluna = int(input("Digite o computador: "))

if 0 <= linha < len(laboratorio) and 0 <= coluna < len(laboratorio[0]):
    if laboratorio[linha][coluna] == "L":
        laboratorio[linha][coluna] = "O"
        print("Computador ocupado com sucesso")
    elif laboratorio[linha][coluna] == "M":
        print("Computador em manutenção")
    else:
        print("Computador já está ocupado")
else:
    print("Posição fora dos limites")

print("MAPA ATUALIZADO")

for linha in laboratorio:
    print(linha)