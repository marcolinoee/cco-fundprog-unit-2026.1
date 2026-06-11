# Dados sugeridos
notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]

# Tarefa 1: Criando lista vazia para os aprovados
aprovados = []

# Tarefa 2 e 3: Filtrando com for e if
for nota in notas:
    if nota >= 7.0:
        aprovados.append(nota)

# Tarefa 4 e Desafio opcional
print("Lista final de aprovados (notas >= 7.0):", aprovados)
print(f"Quantidade de estudantes aprovados: {len(aprovados)}")