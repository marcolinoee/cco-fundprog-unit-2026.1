senha = input("Digite a senha: ")
while True:
    if senha == "Acesso":
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta! Tente novamente.")
        senha = input("Digite a senha: ")