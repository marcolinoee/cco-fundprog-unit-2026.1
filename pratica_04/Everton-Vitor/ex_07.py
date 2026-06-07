# Dados sugeridos
estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"  # Desafio opcional: mude para "Felipe" para testar o 'Não encontrado'

# Tarefa 1: Variável booleana (Flag)
encontrado = False

# Tarefa 2, 3 e 4: Busca com for e interrupção (break)
for estudante in estudantes:
    if estudante == procurado:
        encontrado = True
        break  # Interrompe o laço assim que encontra

# Tarefa 5: Exibição do resultado final
if encontrado:
    print(f"Estudante '{procurado}' foi encontrado(a) na lista!")
else:
    print(f"Estudante '{procurado}' NÃO foi encontrado(a).")