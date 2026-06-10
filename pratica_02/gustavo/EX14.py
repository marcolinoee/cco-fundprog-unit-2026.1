for tentativa in range(1, 101):
    senha = input("Digite a senha: ")
    if senha == "acesso":
        print("Acesso liberado!")
        break
    print("Senha incorreta! Tente novamente.")
else:
    print("Número máximo de tentativas atingido.")

# trocando while por for o codigo fica mais complicado por precisar impor um limite e obrigatoriedade de usar 'break'