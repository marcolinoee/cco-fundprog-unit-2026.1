total = 0

while True:
    valor = float(input("Digite o valor da compra: R$ "))
    total += valor
    
    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    
    if continuar != 'S':
        break

print(f"\nTotal das compras: R$ {total:.2f}")