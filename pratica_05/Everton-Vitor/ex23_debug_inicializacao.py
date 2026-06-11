# 1. Executando e observando a falha de cópia rasa por referência (*):
matriz_incorreta = [[0] * 3] * 3
matriz_incorreta[0][0] = 1
print("Resultado incorreto (referências espelhadas):", matriz_incorreta)

# Explicação em comentário:
# Ao usar [[0] * 3] * 3, o Python cria uma lista interna [0, 0, 0] e multiplica-a criando 
# três referências apontando para O MESMO OBJETO na memória. Mudar uma linha altera todas as outras.

# 3. Criando de forma segura usando compreensão de listas:
matriz_correta = [[0 for coluna in range(3)] for linha in range(3)]

# 4. Testando a alteração na matriz criada com list comprehension:
matriz_correta[0][0] = 1
print("Resultado correto (compreensão de listas):", matriz_correta)

# O que representa cada linha e cada coluna?
# Cada linha e cada coluna representam instâncias isoladas e únicas de memória em formato de grade.