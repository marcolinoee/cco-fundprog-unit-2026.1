from os import system as s


sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]
s('cls')
print(f'Matriz padrão: \n{sala[0]}\n{sala[1]}\n{sala[2]}')
try: 
    linha = int(input('Informe a linha: '))
    coluna = int(input('Informe a coluna: '))
except ValueError:
    print('Valor inválido!')

reserva = sala[linha][coluna]

if reserva == 'L':
    sala[linha][coluna] = 'O'
    print('Reserva realizada!')
elif reserva == 'O':
    print('Assento indisponível!')

print(f'Matriz atualizada: \n{sala[0]}\n{sala[1]}\n{sala[2]}')
    
