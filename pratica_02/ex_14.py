# Exercicio 4

'''def verificarSenha():
    while True:
        
        senha = input("Digite a senha: ")
        if senha == "acesso":
            print("Acesso permitido.")
            break
        else:
            print("Acesso negado.")

verificarSenha()'''

def verificarSenha():
    for _ in iter(int, 1): # Loop infinito usando iter(int, 1)
        senha = input("Digite a senha: ")
        if senha == "acesso":
            print("Acesso permitido.")
            break
        else:
            print("Acesso negado.")

verificarSenha()

# ficou simples, mas o while True é mais comum e fácil de entender. O iter(int, 1) 
# é uma maneira de criar um loop infinito, 
# mas pode ser confuso para quem não está familiarizado com essa técnica. 
# O while True é mais direto e amplamente reconhecido como um loop infinito.
# Eu nem sabia que existia essa técnica, mas é interessante conhecer diferentes 
# formas de criar loops infinitos.