total_compras = 0.0

while True:
    valor = float(input("Digite o valor da compra: "))
    total_compras += valor
    
    continuar = input("Deseja continuar? (S/N): ").upper()
    
    if continuar == 'N':
        break

print(f"Total da compra: R$ {total_compras:.22f}")