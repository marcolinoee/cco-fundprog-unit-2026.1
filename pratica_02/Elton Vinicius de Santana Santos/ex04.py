def ler_Senha():
    while True:
        senha = input("Digite a senha: ")
        if senha == "acesso":
            print("Acesso permitido.")
            break
        else:
            print("Senha incorreta. Tente novamente.")
            return ler_Senha()
ler_Senha()