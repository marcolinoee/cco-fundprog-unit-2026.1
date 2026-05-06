total_compras = 0
quantidade_itens = 0

while True:
    valor = float(input('Digite o valor da compra: R$ '))
    total_compras += valor
    quantidade_itens += 1
    
    continuar = input('Deseja continuar? (S/N): ')
    if continuar == "N":
        break
print('\n--- RESUMO DA COMPRA ---')
print(f'Total de itens: {quantidade_itens}')
print(f'Valor total a pagar: R$ {total_compras:.3f}')
print('Programa encerrado.')
