laboratorio = [
    ["L", "O", "L", "M", "L"],
    ["O", "L", "L", "O", "L"],
    ["L", "L", "M", "L", "O"],
    ["L", "O", "L", "L", "M"]
]

def exibir_mapa(lab):
    for linha in lab:
        print(linha)

exibir_mapa(laboratorio)

livres = ocupados = manutencao = 0
for linha in laboratorio:
    for pc in linha:
        if pc == "L":
            livres += 1
        elif pc == "O":
            ocupados += 1
        else:
            manutencao += 1

print(f"\nLivres: {livres} | Ocupados: {ocupados} | Manutenção: {manutencao}")

linha = int(input("\nDigite a fileira: "))
coluna = int(input("Digite o computador: "))

if linha < 0 or linha >= len(laboratorio) or coluna < 0 or coluna >= len(laboratorio[0]):
    print("Posição fora dos limites.")
elif laboratorio[linha][coluna] == "M":
    print("Computador em manutenção, não pode ser ocupado.")
elif laboratorio[linha][coluna] == "O":
    print("Computador já ocupado.")
else:
    laboratorio[linha][coluna] = "O"
    print("Posição ocupada com sucesso.")

print()
exibir_mapa(laboratorio)