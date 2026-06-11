# Dados sugeridos
frutas = ["maçã", "banana", "uva", "pera"]

# Tarefas 1 e 2: Percorrendo a lista e exibindo a frase
contador_frutas = 0
for fruta in frutas:
    print(f"Eu gosto de {fruta}")
    contador_frutas += 1  # Tarefa 3: Contando manualmente o percurso

print(f"Quantidade de frutas percorridas: {contador_frutas}")

# --- DESAFIO OPCIONAL ---
print("\n--- Desafio: Soletrando Python ---")
for letra in "Python":
    print(f"Letra: {letra}")