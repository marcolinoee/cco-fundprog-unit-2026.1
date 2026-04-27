def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def menu():
    while True:
        print("Menu:")
        print("1. Somar")
        print("2. Subtrair")
        print("0. Exit")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 0:
            print("Saindo...")
            break
        elif opcao == 1:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {somar(n1, n2)}")
        elif opcao == 2:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {subtrair(n1, n2)}")
        else:
            print("Opção inválida.")

menu()
