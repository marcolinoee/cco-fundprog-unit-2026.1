# --- TRECHO A ---
# Explicação do erro: O método .sort() modifica a lista original "in-place" (no local) 
# e retorna None. Ao tentar salvar o retorno em uma variável, ela fica vazia (None).

# Correção do trecho A:
lista = [3, 1, 2]
lista.sort() # Modifica a lista diretamente
resultado = lista # Agora sim, aponta para a lista ordenada
print("Correção A:", resultado)


# --- TRECHO B ---
# Explicação do erro: IndexError. A lista possui apenas 2 elementos (índices 0 e 1). 
# Tentar acessar o índice 5 quebra o programa porque ele não existe.

# Correção do trecho B (Forma segura):
nomes = ["Ana", "Bruno"]
indice_desejado = 5

if indice_desejado < len(nomes):
    print(nomes[indice_desejado])
else:
    print(f"Correção B: O índice {indice_desejado} é inválido para esta lista.")


# --- DESAFIO OPCIONAL (Terceiro Erro Comum) ---
# Erro: Tentar concatenar string com número sem conversão (TypeError)
# Código com erro: idade = 20 -> print("Eu tenho " + idade + " anos")

# Correção do Desafio usando f-string:
idade = 20
print(f"Correção Desafio: Eu tenho {idade} anos.")