notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0]
]

notas[1][0] = 6.5
notas[2][2] = 9.5   

for linha in notas:
    for coluna in linha:
        print(coluna, end=' ')
    print()


valor1 = input("Digite um valor para a primeira nota da segunda linha: ")
valor2 = input("Digite um valor para a terceira nota da terceira linha: ")

notas[1][0] = float(valor1)
notas[2][2] = float(valor2)

for linha in notas:
    for coluna in linha:
        print(coluna, end=' ')
    print()