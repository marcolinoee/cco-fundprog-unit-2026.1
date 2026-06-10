# --- Trecho (a) ---
# Problema: lista.sort() ordena a lista no lugar e retorna None.
# Atribuir o resultado a uma variável faz com que 'resultado' seja None.

# Código com erro:
# lista = [3, 1, 2]
# resultado = lista.sort()
# print(resultado)  -> imprime None

# Correção:
lista = [3, 1, 2]
lista.sort()
print(lista)

# --- Trecho (b) ---
# Problema: a lista 'nomes' tem apenas 2 elementos (índices 0 e 1).
# Acessar nomes[5] causa IndexError pois o índice está fora dos limites.

# Código com erro:
# nomes = ["Ana", "Bruno"]
# print(nomes[5])  -> IndexError

# Correção segura usando verificação antes de acessar:
nomes = ["Ana", "Bruno"]
indice = 5
if indice < len(nomes):
    print(nomes[indice])
else:
    print(f"Índice {indice} fora dos limites. A lista tem {len(nomes)} elemento(s).")

# --- Trecho extra (c) ---
# Problema: tentar concatenar string com número diretamente causa TypeError.

# Código com erro:
# idade = 20
# print("Idade: " + idade)  -> TypeError

# Correção:
idade = 20
print("Idade: " + str(idade))
