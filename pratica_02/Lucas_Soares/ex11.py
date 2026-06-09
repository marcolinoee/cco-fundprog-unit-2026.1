aprovados = 0
recuperacao = 0
reprovados = 0


while True: 
    quantidade = (input("Digite a quantidade de alunos: "))
    try:
        quantidade_int = int(quantidade)
        break
    except:
        print('Digite um numero')
        continue

for aluno in range(quantidade_int):
    while True:
        try:
            media = float(input(f"Digite a média do {aluno+1}º aluno (0 a 10): "))
            
            if 0 <= media <= 10:
                break 
            else:
                print("Valor inválido! Digite uma nota entre 0 e 10.")
        
        except :
            print("Entrada inválida! Digite um número válido.")

    if media >= 7:
        aprovados += 1
    elif media >= 4:
        recuperacao += 1
    else:
        reprovados += 1

print("Resultado final:")
print("Aprovados:", aprovados)
print("Recuperação:", recuperacao)
print("Reprovados:", reprovados)