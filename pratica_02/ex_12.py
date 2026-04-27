compras = []

while True:
    valorDaCompra = input("Digite o valor do produto: ")
    compras.append(valorDaCompra)

    sair = input("Deseja encerrar as compras? (S/N): ")
    if sair.lower() == 's':
        
        print("Lista de compras:")
        for i, compra in enumerate(compras, start=1):
            print(f"{i}. {compra}")
        break
    elif sair.lower() == 'n':
        continue
    