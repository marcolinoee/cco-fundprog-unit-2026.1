ano_atual = 2026
nome_usuario = str(input('Informe seu nom de usuario: '))
ano_nascimnto = int(input('Informe seu ano d nascimento: '))
idade = ano_atual - ano_nascimnto
altura_str = str(input('Informe sua altura: '))
altura_float = float(altura_str)

print(f'Olá {nome_usuario} ! Você tem {idade} anos e sua altura é de {altura_float}, Resgistro concluido!')
