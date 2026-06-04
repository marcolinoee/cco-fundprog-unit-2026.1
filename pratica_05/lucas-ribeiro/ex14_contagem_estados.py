sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]
assentos_livres = 0
assentos_ocupados = 0
total_assentos = 0
for linha in sala:
    for assento in linha:
        if assento == 'L':
            assentos_livres += 1
            total_assentos += 1
        elif assento == 'O':
            assentos_ocupados += 1
            total_assentos += 1
        else:
            continue

print(f'Total de Assentos: {total_assentos}\nAssentos Livres: {assentos_livres}\nAssentos Ocupados: {assentos_ocupados}')
 