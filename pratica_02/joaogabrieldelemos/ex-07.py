soma_par = 0
num_par = 0
for i in range (1,9):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        soma_par += num
        num_par += 1
print (f'Foram digitados {num_par} números pares.')
print (f'E a soma dos números pares é de: {soma_par}.')
