senha_certa = 'acesso'
while True:
    tentativa = input('Digite sua senha ')

    if tentativa == senha_certa:
        print('Voce entrou')
        break
    else:
        print('Senha incorreta')
        continue