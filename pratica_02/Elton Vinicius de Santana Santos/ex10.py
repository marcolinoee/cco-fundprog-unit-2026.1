class Menu:
    def __init__(self):
        pass

    def exibir_menu(self):
        print("\n1 - Somar")
        print("2 - Subtrair")
        print("3 - Sair")

    def escolher_opcao(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.somar()
            elif opcao == "2":
                self.subtrair()
            elif opcao == "3":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def somar(self):
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))
        print("Resultado:", a + b)

    def subtrair(self):
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))
        print("Resultado:", a - b)

menu = Menu()
menu.escolher_opcao()