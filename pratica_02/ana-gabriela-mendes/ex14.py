senha = input("Digite a senha: ")

for i in range(3):
    if senha == "Acesso":
        print("Acesso concedido.")
        break
    print("Acesso negado.")
    senha = input("Digite a senha: ")

# Ficou mais fácil de entender a lógica do programa, pq o loop for já limita o número de tentativas a 3, e o break garante que o programa pare assim que a senha correta for digitada.