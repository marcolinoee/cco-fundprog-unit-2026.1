sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

print("Mapa de assentos inicial:")
for linha in sala:
    print(linha)

# Desafio extra: Laço de repetição contínuo até -1 ser digitado
while True:
    print("\n--- Sistema de Reservas (Digite -1 na linha para sair) ---")
    lin = int(input("Digite a linha: "))
    if lin == -1:
        print("Saindo do sistema de reservas.")
        break
        
    col = int(input("Digite a coluna: "))
    
    # Validação de limites
    if 0 <= lin < len(sala) and 0 <= col < len(sala[0]):
        if sala[lin][col] == "L":
            sala[lin][col] = "O"
            print("Reserva realizada.")
        else:
            print("Assento indisponível.")
    else:
        print("Erro: Esta posição não existe na sala!")
        
    print("\nMapa atualizado:")
    for linha in sala:
        print(linha)

# O que representa cada linha e cada coluna?
# As linhas e colunas representam o mapeamento espacial geométrico das cadeiras para reserva.