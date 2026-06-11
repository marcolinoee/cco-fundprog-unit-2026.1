notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
aprovados = []
# aprovados = [nota for nota in notas if nota >= 7] --> Sem utilizar o .append()

for nota in notas:
    if nota >= 7:
        aprovados.append(nota)
    else:
        continue


print(f'Lista de aprovados: {aprovados}\nQuantidade de aprovados: {len(aprovados)}')





