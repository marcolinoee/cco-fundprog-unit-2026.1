# Dados fornecidos
palavra = "programacao"
valores = [10, 20, 30, 40, 50, 60]

# --- TAREFAS ---

# 1. Exiba os 4 primeiros caracteres da palavra.
# (Do índice 0 até o 4, sem incluir o 4)
print("1. 4 primeiros caracteres:", palavra[0:4])  # Ou apenas palavra[:4]

# 2. Exiba os caracteres da posição 4 até a 8.
# (Lembrando que o índice 8 não entra no resultado, então vai do 4 ao 7)
print("2. Posição 4 até 8:", palavra[4:8])

# 3. Exiba os três primeiros elementos da lista.
# (Do índice 0 até o 3)
print("3. Três primeiros elementos:", valores[:3])

# 4. Exiba os elementos da posição 2 até o final da lista.
# (Deixando o espaço após os dois pontos vazio, ele vai até o fim)
print("4. Posição 2 até o final:", valores[2:])


# --- DESAFIO OPCIONAL (Observações sobre fatiamento) ---

# Observação 1: O terceiro argumento é o 'passo' (step). 
# palavra[::2] pega a string inteira pulando de 2 em 2 caracteres.
print("\nDesafio - Passo 2:", palavra[::2])

# Observação 2: Índices negativos contam a partir do final da sequência.
# valores[-2:] pega os dois últimos elementos da lista.
print("Desafio - Dois últimos:", valores[-2:])

# Observação 3: Inversão de sequência usando passo negativo (-1).
print("Desafio - Palavra invertida:", palavra[::-1])