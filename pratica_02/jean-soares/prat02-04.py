# While - Python
senha_correta = "acesso"
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = input("Digite a senha para liberar acesso: ")
    
    if senha_digitada == senha_correta:
        print("✓ Acesso liberado!")
    else:
        print("✗ Senha incorreta. Tente novamente.")