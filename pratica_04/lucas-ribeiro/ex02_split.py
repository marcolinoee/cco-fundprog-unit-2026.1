nome_completo = "Maria Clara Souza"

lista_letras_nome = [nome for nome in nome_completo.split()]

print(lista_letras_nome)
print('-'.join(nome_completo))
print(f'Primeiro nome: {nome_completo[0:5]}\nÚltimo sobrenome: {nome_completo[-5:]}')