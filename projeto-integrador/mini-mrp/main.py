#Nicolas D. e Laura R. - Menu e MPS // POO do chão de fábrica
def exibir_menu():
    print("\n" + "="*30)
    print("   SISTEMA MRP - APPLE IND.   ")
    print("="*30)
    print("1. Inserir demanda de iPhone")
    print("2. Ver plano de produção")
    print("3. Executar motor de explosão")
    print ("4. Sair")
   

def main ():
    produto = []
    quantidade_pedida = 0
    semana_entrega = 0
    pedido_existe = False
Estoque_baterias = 100
estoque_telas = 100
estoque_processadores = 100
estoque_carcacas = 100
estoque_memorias = 100
bateria = 0
tela = 0
processador = 0
carcaca = 0
memoria = 0

while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = input("Modelo do iPhone (Ex: iPhone 15): ")

            quantidade_pedida = int(input("Quantidade: "))
            while quantidade_pedida <= 0:
                print("Erro. Quantidade deve ser maior que 0. Tente novamente.")
                quantidade_pedida = int(input("Quantidade: "))

            semana_entrega = int(input("Semana de entrega (1-8): "))
            while semana_entrega < 1 or semana_entrega > 8:
                print("Erro. A semana de entrega deve ser entre 1 e 8. Tente novamente.")
                semana_entrega = int(input("Semana de entrega (1-8): "))
            
            pedido_existe = True
            print(f"\n Demanda de {quantidade_pedida} unidades de {produto} para a semana {semana_entrega} registrada.")      
        elif opcao == "2":
            if pedido_existe:
                print("\n--- RESUMO DO PLANO MESTRE ---")
                print(f"produto: {produto}")
                print(f"Volume: {quantidade_pedida} unidades")
                print(f"Prazo: Semana {semana_entrega}")
            else:
                print("\nNenhuma demanda registrada. Por favor, insira uma demanda primeiro.")
            if opcao == "3":
                if pedido_existe:
                    print("\n--- EXECUTANDO MOTOR DE EXPLOSÃO ---")
                    print(f"Processando demanda de {quantidade_pedida} unidades de {produto} para a semana {semana_entrega}...")
                    def motor_explosao(produto_cadastrado):
                        
                        print("\n---PROCESSANDO MOTOR DE EXPLOSÃO---")
#Laura R. - Motor de explosão
item_novo["quantidade"][0]
quantidade_fabricacao = produto_cadastrado["quantidade"][0]
componentes = produto_cadastrado["nome"]
estoques = produto_cadastrado["estoque"]
print(f"Demanda de produção:{quantidade_pedida} Iphones" )
print("-" * 30)

for i in range(len(componentes)):
       nome_item = componentes[i]
       estoque = componentes[i]
       necessidade = quantidade_fabricacao

       saldo = estoque - necessidade

       if saldo < 0:
         print(f"Item: {nome_item} insuficiente. Faltam {abs(saldo)} unidades.")
else:
          print(f"Item: {nome_item} | Necessário: {necessidade} | Saldo após produção: {saldo}")   

while True:
    if opcao == "4":
        print("encerrando o programa...")
        break

       
if __name__ == "__main__":
    main() 


def main():
    produto = []
    quantidade_pedida = 0
    semana_entrega = 0
    pedido_existe = False
item_novo = { 
    "nome": [bateria, tela, processador, carcaca, memoria],
    "quantidade": [quantidade_pedida],
    "estoque": [estoque_carcacas, estoque_memorias, estoque_processadores, estoque_telas, Estoque_baterias]
}
while True:
  produto.append(item_novo)

cadastro = input("Deseja cadastrar mais itens? (s/n): ")
if cadastro.lower() == "n":
    print("Encerrando programa...")
   









#Nicolas G. -