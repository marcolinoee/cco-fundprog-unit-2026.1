from os import system as s

total = 0
while True:
    valor_compra = float(input('Informe qual o valor que deseja pagar: R$ '))
    total += valor_compra

    opcao = str(input('Deseja continuar a operação (S/N): ').upper())
    if opcao == 'S':
        continue
    elif opcao == 'N':
        break
    else:
        print('Operação selecionada inválida!')
        
print(f'O total de suas compras é de R${total:.2f}.\n\nObrigado por utilizar o programa!')