soma_par = 0
num_par = 0
for i in range(1, 9):
    num = int(input(f"Digite o {i}º valor: "))
    
    if num % 2 == 0:
        num_par += 1
        soma_par += num
print(f'Foram digitados {num_par} números pares')
print(f"A soma dos pares é: {soma_par}")

#Ficou mais fácil de ler, o código ficou com menos linhas e mais organizado.