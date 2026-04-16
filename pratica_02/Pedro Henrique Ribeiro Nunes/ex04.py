senha = str(input('Digite a senha: '))
while True:
    if senha != '1234pedro':
        print('Senha inválida.')
        senha = int(input('Digite novamente: '))
    else:
        print('Senha correta.\nAcesso autorizado.')
        break
