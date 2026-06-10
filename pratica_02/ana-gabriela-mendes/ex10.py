opcao = -1

while opcao != 0:
    print("Menu de opções:")
    print("1. somar")
    print("2. subtrair")
    print("0. sair")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        num1 = int(input("Digite o Número 1: "))
        num2 = int(input("Digite o Número 2: "))
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado}")

    elif opcao == 2:
        num3 = int(input("Digite o Número 1: "))
        num4 = int(input("Digite o Número 2: "))
        resultado = num3 - num4
        print(f"Resultado da subtração: {resultado}")

    elif opcao == 0:
        print("Saindo do programa.")

    else:
        print("Opção inválida. Tente novamente.")