def inicializar_estoque():
    return [
        {"nome": "Bateria", "estoque": 100},
        {"nome": "Tela", "estoque": 100},
        {"nome": "Processador", "estoque": 100},
        {"nome": "Carcaça", "estoque": 100},
        {"nome": "Memória", "estoque": 100}
    ]

#MOTOR DE EXPLOSÃO
def executar_motor_explosao(quantidade_pedida, componentes):
    print("\n" + "-"*40)
    print(f"EXECUTANDO EXPLOSÃO PARA {quantidade_pedida} UNIDADES")
    print("-"*40)
    
    for item in componentes:
        nome_item = item["nome"]
        estoque_atual = item["estoque"]
        necessidade = quantidade_pedida # Proporção 1:1
        
        saldo_pos_producao = estoque_atual - necessidade
        
        if saldo_pos_producao < 0:
            print(f"Item: {nome_item:12} | [FALTA] {abs(saldo_pos_producao)} unidades")
        else:
            print(f"Item: {nome_item:12} | [OK] Saldo final: {saldo_pos_producao}")

#Planilha
def mostrar_planilha(necessidades):
    semanas = 8

    print("\n--- PLANILHA DE NECESSIDADES ---")

    print("Componente".ljust(15), end="")
    for i in range(1, semanas + 1):
        print(f"S{i}".rjust(5), end="")
    print()

    print("-" * (15 + semanas * 5))

    for componente, valores in necessidades.items():
        print(componente.ljust(15), end="")
        for v in valores:
            print(str(v).rjust(5), end="")
        print()

def exibir_menu():
    print("\n" + "="*35)
    print("      SISTEMA MRP - APPLE IND.     ")
    print("="*35)
    print("1. Inserir demanda de iPhone")
    print("2. Ver plano de produção (MPS)")
    print("3. Executar motor de explosão")
    print("4. Sair")
    print("="*35)

def main():
    estoque_central = inicializar_estoque()
    modelo_iphone = ""
    quantidade_pedida = 0
    semana_entrega = 0
    pedido_existe = False

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            modelo_iphone = input("Modelo do iPhone (Ex: iPhone 15): ")
            
            quantidade_pedida = int(input("Quantidade: "))
            while quantidade_pedida <= 0:
                print("Erro: A quantidade deve ser maior que 0.")
                quantidade_pedida = int(input("Quantidade: "))
            semana_entrega = int(input("Semana de entrega (1-8): "))
            while semana_entrega < 1 or semana_entrega > 8:
                print("Erro: Prazo deve ser entre a semana 1 e 8.")
                semana_entrega = int(input("Semana de entrega (1-8): "))
            
            pedido_existe = True
            print(f"\n[!] Demanda de {quantidade_pedida} unidades registrada com sucesso.")

        elif opcao == "2":
            if pedido_existe:
                print("\n--- PLANO MESTRE DE PRODUÇÃO (MPS) ---")
                print(f"PRODUTO:  {modelo_iphone}")
                print(f"VOLUME:   {quantidade_pedida} unidades")
                print(f"PRAZO:    Semana {semana_entrega}")
            else:
                print("\n[!] Erro: Nenhuma demanda cadastrada. Use a opção 1.")

        elif opcao == "3":
            if pedido_existe:
                executar_motor_explosao(quantidade_pedida, estoque_central)
                 # PLANILHA
                necessidades = {
                    "Bateria": [0, 0, quantidade_pedida, 0, 0, 0, 0, 0],
                    "Tela": [0, 0, quantidade_pedida, 0, 0, 0, 0, 0],
                    "Processador": [0, 0, quantidade_pedida, 0, 0, 0, 0, 0],
                    "Carcaça": [0, 0, quantidade_pedida, 0, 0, 0, 0, 0],
                    "Memória": [0, 0, quantidade_pedida, 0, 0, 0, 0, 0],
                }

                mostrar_planilha(necessidades)

            else:
                print("\n[!] Erro: Defina a demanda antes de executar o motor.")

        elif opcao == "4":
            print("Encerrando o programa... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
if __name__ == "__main__":
    main()