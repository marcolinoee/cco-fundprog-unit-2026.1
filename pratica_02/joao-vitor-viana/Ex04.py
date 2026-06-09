
senha = ''
while senha.lower() != 'acesso':
    senha = input('Digite a sua senha: ')

    if senha.lower() != 'acesso':
        print('Senha incorreta! Tente novamente.')
print('Acesso concedido. Bem-vindo!')
