import os 
os.system("cls")  

while True:
    print("\n--- MENU ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        print(f"Resultado: {a + b}")

    elif opcao == 2:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        print(f"Resultado: {a - b}")

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        os.system("cls") 