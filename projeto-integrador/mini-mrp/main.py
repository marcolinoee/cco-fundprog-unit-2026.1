def inicializar_estoque():
    componentes = [
        {"nome": "Item 1", "estoque": 100},
        {"nome": "Item 2", "estoque": 100},
        {"nome": "Item 3", "estoque": 100},
        {"nome": "Item 4", "estoque": 100},
        {"nome": "Item 5", "estoque": 100}
    ] 
    return componentes
#MOTOR DE EXPLOSÃO
def executar_motor_explosao(quantidade_pedida, componentes):
    print("\n" + "-"*40)
    print(f"EXECUTANDO EXPLOSÃO PARA {quantidade_pedida} UNIDADES")
    print("-"*40)
    
    for item  in componentes:
        nome_item = item["nome"]
        estoque_atual = item["estoque"]
        necessidade = quantidade_pedida 
        
        saldo_pos_producao = estoque_atual - necessidade
        
        if saldo_pos_producao < 0:
            print(f"Item: {nome_item:12} | [FALTA] {abs(saldo_pos_producao)} unidades")
        else:
            print(f"Item: {nome_item:12} | [OK] Saldo final: {saldo_pos_producao}")

#Planilha
def mostrar_planilha(necessidade, semana_entrega):
    total_semanas = 8
    print("")
    print("==============================================================")
    print("\n--- PLANILHA DE NECESSIDADES ---")
    print("==============================================================")

    cabecalho = "componente   "
    for semana in range(1, total_semanas + 1):
        cabecalho = cabecalho + "S" + str(semana) + "   "
    print(cabecalho)
    print("-"*60)

    for nome in necessidade:
        linha = nome + "   "
        for semana in range(1, total_semanas + 1):
            if semana == semana_entrega:
                valor = necessidade [nome]
            else:
                valor = 0
            linha = linha + str(valor) + "   "
        print(linha)
        print("-"*60)


def exibir_menu():
    print("\n" + "="*35)
    print("      SISTEMA MRP     ")
    print("="*35)
    print("1. Inserir produto")
    print("2. Ver plano de produção (MPS)")
    print("3. Executar motor de explosão")
    print("4. Sair")
    print("="*35)

def main():
    estoque_central = inicializar_estoque()
    nome_produto = ""
    quantidade_pedida = 0
    semana_entrega = 0
    pedido_existe = False

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_produto = input("Insira o produto: ")
            
            quantidade_pedida = int(input("Quantidade: "))
            while quantidade_pedida <= 0:
                print("Erro: A quantidade deve ser maior que 0.")
                quantidade_pedida = int(input("Quantidade: "))
            semana_entrega = int(input("Semana de entrega (1-8): "))
            while semana_entrega < 1 or semana_entrega > 8:
                print("Erro: Prazo deve ser entre a semana 1 e 8.")
                semana_entrega = int(input("Semana de entrega (1-8): "))
            
            pedido_existe = True
            print(f"\n[!] Demanda de {quantidade_pedida} unidades de {nome_produto} registrada com sucesso.")

        elif opcao == "2":
            if pedido_existe:
                print("\n--- PLANO MESTRE DE PRODUÇÃO (MPS) ---")
                print(f"PRODUTO:  {nome_produto}")
                print(f"VOLUME:   {quantidade_pedida} unidades")
                print(f"PRAZO:    Semana {semana_entrega}")
            else:
                print("\n[!] Erro: Nenhuma demanda cadastrada. Use a opção 1.")

        elif opcao == "3":
            if pedido_existe:
                executar_motor_explosao(quantidade_pedida, estoque_central)
                 # PLANILHA
                necessidade = {
                    "Item 1": quantidade_pedida, 
                    "Item 2": quantidade_pedida, 
                    "Item 3": quantidade_pedida, 
                    "Item 4": quantidade_pedida,
                    "Item 5": quantidade_pedida, 
                }

                mostrar_planilha(necessidade, semana_entrega,)

            else:
                print("\n[!] Erro: Defina a demanda antes de executar o motor.")

        elif opcao == "4":
            print("Encerrando o programa... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
if __name__ == "__main__":
    main()