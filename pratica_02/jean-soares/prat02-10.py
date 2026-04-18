# Menu de operações - Python

while True:
    print("Menu de operações:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")

    opcao = int(input("Digite a opção desejada (1, 2 ou 0): "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"Resultado: {num1 + num2}")

    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"Resultado: {num1 - num2}")

    elif opcao == 0:
        print("Encerrado. Até mais!")

    else:
        Print("Opção inválida! Tente digitar 1, 2 ou 0.")