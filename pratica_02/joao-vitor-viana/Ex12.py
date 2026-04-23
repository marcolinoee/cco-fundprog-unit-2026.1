total_gasto = 0

while True:
    valor_compra = float(input("Digite o valor da compra: R$ "))
    
    # Atualiza nossos dados
    total_gasto += valor_compra
    
    # Pergunta se o usuário quer continuar
    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    
    # Verifica a condição de parada
    if continuar == 'N':
        break

print("-" * 30)
print(f"Total da compra: R$ {total_gasto:.2f}")
print("Programa encerrado. Volte sempre!")