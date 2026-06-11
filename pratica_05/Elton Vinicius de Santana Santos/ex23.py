matriz = [[0] * 3] * 3
matriz[0][0] = 1

print(matriz)

print("Resposta 1: Todas as linhas foram alteradas na primeira coluna.")
print("Resposta 2: Isso acontece porque as linhas compartilham a mesma referência na memória.")

matriz = [[0 for coluna in range(3)] for linha in range(3)]

matriz[0][0] = 1

print(matriz)

print("Resposta 3: Agora apenas a célula matriz[0][0] foi alterada.")