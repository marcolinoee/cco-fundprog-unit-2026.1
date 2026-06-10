senha = input('Insira a senha correta: ').lower()

while senha != "acesso":
    senha = input(('Senha incorreta! insira a senha correta: ')).lower()

print('Acesso concedido')