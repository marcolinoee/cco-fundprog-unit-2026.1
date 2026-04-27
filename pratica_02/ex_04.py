def verificarSenha():
    while True:
        
        senha = input("Digite a senha: ")
        if senha == "acesso":
            print("Acesso permitido.")
            break
        else:
            print("Acesso negado.")

verificarSenha()