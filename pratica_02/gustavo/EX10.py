opcao = -1

while opcao != 0:
    print("=== MENU ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado: {}".format(a + b))

    elif opcao == 2:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado: {}".format(a - b))

    elif opcao != 0:
        print("Opção inválida!")
    
    print()

print("Encerrando o programa. Até logo!")