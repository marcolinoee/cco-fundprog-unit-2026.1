sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

livres = 0
ocupados = 0

for linha in sala:
    for assento in linha:
        if assento == "L":
            livres += 1
        elif assento == "O":
            ocupados += 1

print(f"Assentos livres: {livres}")
print(f"Assentos ocupados: {ocupados}")

# --- DESAFIO EXTRA ---
total_assentos = livres + ocupados
percentual_ocupacao = (ocupados / total_assentos) * 100
print(f"Percentual de ocupação da sala: {percentual_ocupacao:.2f}%")

# O que representa cada linha e cada coluna?
# Cada linha representa uma fileira física de assentos no estabelecimento/cinema.
# Cada coluna representa a posição exata da cadeira dentro de sua respectiva fileira.s