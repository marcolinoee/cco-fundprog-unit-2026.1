# Exercício 12: Registro de Compras (Interatividade)

total = 0
quantidadeCompras = 0

while True:
    valor = float(input("Digite o valor da compra: "))
    
    # Acumular
    total += valor
    quantidadeCompras += 1
    
    continuar = input("Deseja continuar? (S/N): ")
    
    if continuar == "N":
        break

print("Resultado das compras:")
print(f"Quantidade de compras: {quantidadeCompras}")
print(f"Total gasto: R${total}")