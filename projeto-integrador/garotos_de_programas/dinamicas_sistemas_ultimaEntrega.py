import os

class Usina:
    def __init__(self):
        self.producao_energia = 5000
        self.poluicao_gerada = 50
        self.custo_manutencao = 0

class EstacaoAgua:
    def __init__(self):
        self.producao_agua = 10000
        self.custo_manutencao = 0

class Hospital:
    def __init__(self):
        self.custo_manutencao = 0

class Cidade:
    def __init__(self, populacao_inicial, caixa_inicial):
        self.populacao = populacao_inicial
        self.caixa = caixa_inicial
        self.ano_atual = 1
        self.poluicao_acumulada = 0
        self.usinas = []
        self.estacoes_agua = []
        self.hospitais = []
        self.historico_anos = []
        self.historico_populacao = []
        self.relatorio_crise = self.gerar_relatorio_inicial()

    def gerar_relatorio_inicial(self):
        return {
            "demanda_energia": 2000,
            "capacidade_energia": 5000,
            "demanda_agua": 3000,
            "capacidade_agua": 10000,
            "crise_hidrica": False,
            "crise_energetica": False
        }

    def calcular_energia_total(self):
        return sum(usina.producao_energia for usina in self.usinas)

    def calcular_agua_total(self):
        return sum(estacao.producao_agua for estacao in self.estacoes_agua)

    def salvar_historico(self):
        self.historico_anos.append(self.ano_atual)
        self.historico_populacao.append(self.populacao)

    def processar_ano(self):
        demanda_energia = self.populacao * 2
        demanda_agua = self.populacao * 3
        
        capacidade_energia = self.calcular_energia_total()
        capacidade_agua = self.calcular_agua_total()
        
        self.poluicao_acumulada += len(self.usinas) * 50
        
        taxa_mortalidade = 0.02
        modificador_arrecadacao = 1.0
        
        crise_hidrica = demanda_agua > capacidade_agua
        if crise_hidrica:
            taxa_mortalidade *= 2
            
        crise_energetica = demanda_energia > capacidade_energia
        if crise_energetica:
            modificador_arrecadacao = 0.5
            
        arrecadacao = (self.populacao * 10) * modificador_arrecadacao
        self.caixa += arrecadacao
        
        nascimentos = self.populacao * 0.05
        mortes_naturais = self.populacao * taxa_mortalidade
        nova_pop = self.populacao + nascimentos - mortes_naturais
        
        if self.poluicao_acumulada > 1000 and not self.hospitais:
            mortes_poluicao = nova_pop * 0.10
            nova_pop -= mortes_poluicao
            
        self.populacao = int(nova_pop)
        self.ano_atual += 1
        
        self.relatorio_crise = {
            "demanda_energia": demanda_energia,
            "capacidade_energia": capacidade_energia,
            "demanda_agua": demanda_agua,
            "capacidade_agua": capacidade_agua,
            "crise_hidrica": crise_hidrica,
            "crise_energetica": crise_energetica
        }

    def construir_usina(self, custo):
        if self.caixa >= custo:
            self.usinas.append(Usina())
            self.caixa -= custo
            return True
        return False

    def construir_estacao_agua(self, custo):
        if self.caixa >= custo:
            self.estacoes_agua.append(EstacaoAgua())
            self.caixa -= custo
            return True
        return False

    def construir_hospital(self, custo):
        if self.caixa >= custo:
            self.hospitais.append(Hospital())
            self.caixa -= custo
            return True
        return False

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_grafico_ascii(cidade):
    print("\nEVOLUCAO DA POPULACAO")
    if not cidade.historico_anos:
        print("Nenhum dado registrado.")
        return
        
    for ano, pop in zip(cidade.historico_anos, cidade.historico_populacao):
        escala = pop // 100
        barras = "*" * escala
        print(f"Ano {ano:02d}: [{pop:4d} hab] {barras}")
    input("\nPressione [ENTER] para voltar ao menu...")

def exibir_painel(cidade):
    print(f"GOVERNO DA CIDADE - ANO: {cidade.ano_atual}")
    print(f"Populacao: {cidade.populacao} hab")
    print(f"Caixa: R$ {cidade.caixa:,.2f}")
    print(f"Poluicao Acumulada: {cidade.poluicao_acumulada} pontos")
    print(f"Usinas de Carvao: {len(cidade.usinas)} | Estacoes de Agua: {len(cidade.estacoes_agua)} | Hospitais: {len(cidade.hospitais)}")
    print("-" * 50)
    
    relatorio = cidade.relatorio_crise
    status_energia = "CRISE!" if relatorio["crise_energetica"] else "OK"
    status_agua = "CRISE!" if relatorio["crise_hidrica"] else "OK"
    
    print(f"Energia: {relatorio['demanda_energia']} / {relatorio['capacidade_energia']} kWh [{status_energia}]")
    print(f"Agua: {relatorio['demanda_agua']} / {relatorio['capacidade_agua']} L [{status_agua}]")
    print("-" * 50)

def iniciar_jogo():
    cidade_jogo = Cidade(populacao_inicial=1000, caixa_inicial=50000)
    cidade_jogo.usinas.append(Usina())
    cidade_jogo.estacoes_agua.append(EstacaoAgua())
    
    cidade_jogo.salvar_historico()
    
    custo_usina = 20000
    custo_agua = 15000
    custo_hospital = 25000

    while cidade_jogo.populacao > 0 and cidade_jogo.ano_atual <= 50:
        limpar_tela()
        exibir_painel(cidade_jogo)

        while True:
            print("\nOPCOES DE ACAO:")
            print(f"1 - Construir Usina (R$ {custo_usina})")
            print(f"2 - Construir Estacao de Agua (R$ {custo_agua})")
            print(f"3 - Construir Hospital (R$ {custo_hospital})")
            print("4 - Visualizar Grafico de Evolucao")
            print("5 - Avancar Ano")

            entrada = input("Escolha uma opcao: ")

            if not entrada.isdigit():
                print("Digite apenas numeros.")
                continue

            escolha = int(entrada)

            if escolha == 1:
                if cidade_jogo.construir_usina(custo_usina):
                    print("Usina construida com sucesso.")
                else:
                    print("Recursos financeiros insuficientes.")
            elif escolha == 2:
                if cidade_jogo.construir_estacao_agua(custo_agua):
                    print("Estacao de agua construida com sucesso.")
                else:
                    print("Recursos financeiros insuficientes.")
            elif escolha == 3:
                if cidade_jogo.construir_hospital(custo_hospital):
                    print("Hospital construido com sucesso.")
                else:
                    print("Recursos financeiros insuficientes.")
            elif escolha == 4:
                exibir_grafico_ascii(cidade_jogo)
                break
            elif escolha == 5:
                cidade_jogo.processar_ano()
                cidade_jogo.salvar_historico()
                break
            else:
                print("Opcao invalida.")

    limpar_tela()
    print("FIM DE JOGO")
    if cidade_jogo.populacao <= 0:
        print("GAME OVER - Sua populacao foi reduzida a zero.")
    else:
        print(f"PARABENS! Voce sobreviveu aos 50 anos de mandato com {cidade_jogo.populacao} habitantes.")
        
    exibir_grafico_ascii(cidade_jogo)

if __name__ == '__main__':
    iniciar_jogo()