fez_soma = False
fez_subtracao = False
pediu_sair = False

print("terminal interativo de soma e subtração")

while not (fez_soma and fez_subtracao and pediu_sair):
    print("\n--- MENU ---")
    print("1. somar dois numeros")
    print("2. subtrair dois numeros")
    print("3. sair")
    
    opcao = input("escolha uma opção: ")
    
    if opcao == "1":
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input("digite o segundo numero: "))
        resultado = num1 + num2
        print(f"o resultado da soma é: {resultado}")
        fez_soma = True
    elif opcao == "2":
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input("digite o segundo numero: "))
        resultado = num1 - num2
        print(f"o resultado da subtração é: {resultado}")
        fez_subtracao = True
    elif opcao == "3":
        if fez_soma and fez_subtracao:
            print("obrigado por usar o terminal interativo!")
            pediu_sair = True
        else:
            print("você precisa realizar pelo menos uma soma e uma subtração antes de sair.")
    else:
        print("opção inválida, por favor escolha uma opção válida.")