nomes = ["Ana", "Bruno", "Carla", "Diego"]
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

maior_media = -1
nome_maior = ""

menor_media = 11  # Para o desafio extra
nome_menor = ""

for i in range(len(notas)):
    media = sum(notas[i]) / len(notas[i])
    
    if media > maior_media:
        maior_media = media
        nome_maior = nomes[i]
        
    if media < menor_media:
        menor_media = media
        nome_menor = nomes[i]

print(f"Maior média: {nome_maior} - {maior_media:.2f}")
print(f"Desafio - Menor média: {nome_menor} - {menor_media:.2f}")

# O que representa cada linha e cada coluna?
# Cada linha representa as notas individuais de um indivíduo do corpo estudantil.
# Cada coluna representa o desempenho da turma em avaliações padronizadas.