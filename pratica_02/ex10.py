op = -1
while op != 0:
    print ("\--- MENU DE OPERAÇÕES ---")
    print ("1 - Soma")
    print ("2 - Subtrair")
    print ("0 - Sair")
    op = int(input("Escolha uma opção: "))
    if op == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado: " + str(n1+n2))
    elif op == 2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado: " + str(n1-n2))
    elif op == 0:
        print("Encerrando o programa. Até logo!")