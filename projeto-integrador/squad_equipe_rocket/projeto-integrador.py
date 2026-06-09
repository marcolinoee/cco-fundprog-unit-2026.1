# DASHBOARD FINANCEIRO - PROJETO 15

# ALUNO 3 - JOÃO GABRIEL

class DemonstracaoAnual:
    def __init__(self, ano, ativo_circulante, estoques, ativo_nao_circ,
                 passivo_circulante, passivo_nao_circ, passivo_total,
                 patrimonio_liquido, receita_liquida, lucro_liquido):

        # Dados brutos
        self.ano                = ano
        self.ativo_circulante   = ativo_circulante
        self.estoques           = estoques
        self.ativo_nao_circ     = ativo_nao_circ
        self.ativo_total        = ativo_circulante + ativo_nao_circ
        self.passivo_circulante = passivo_circulante
        self.passivo_nao_circ   = passivo_nao_circ
        self.passivo_total      = passivo_total
        self.patrimonio_liquido = patrimonio_liquido
        self.receita_liquida    = receita_liquida
        self.lucro_liquido      = lucro_liquido

        # Indicadores financeiros - Rafael Varella
        
        self.liquidez_corrente  = self._liquidez_corrente()
        self.liquidez_seca      = self._liquidez_seca()
        self.margem_liquida     = self._margem_liquida()
        self.roe                = self._roe()
        self.endividamento      = self._endividamento()

    # Parte do motor analitico - Rafael Varella

    def _liquidez_corrente(self):
        if self.passivo_circulante == 0:
            return None
        return self.ativo_circulante / self.passivo_circulante

    def _liquidez_seca(self):
        if self.passivo_circulante == 0:
            return None
        return (self.ativo_circulante - self.estoques) / self.passivo_circulante

    def _margem_liquida(self):
        if self.receita_liquida == 0:
            return None
        return self.lucro_liquido / self.receita_liquida

    def _roe(self):
        if self.patrimonio_liquido == 0:
            return None
        return self.lucro_liquido / self.patrimonio_liquido

    def _endividamento(self):
        total = self.passivo_total + self.patrimonio_liquido
        if total == 0:
            return None
        return self.passivo_total / total

    def exibir_resumo(self):
        print(f"\n  Ano: {self.ano}")
        print(f"  Ativo Total:        R$ {self.ativo_total:,.2f}")
        print(f"  Receita Líquida:    R$ {self.receita_liquida:,.2f}")
        print(f"  Lucro Líquido:      R$ {self.lucro_liquido:,.2f}")
        print(f"  Liquidez Corrente:  {self.liquidez_corrente:.4f}" if self.liquidez_corrente is not None else "  Liquidez Corrente: N/A")
        print(f"  Liquidez Seca:      {self.liquidez_seca:.4f}"      if self.liquidez_seca      is not None else "  Liquidez Seca: N/A")
        print(f"  Margem Líquida:     {self.margem_liquida:.4f}"     if self.margem_liquida     is not None else "  Margem Líquida: N/A")
        print(f"  ROE:                {self.roe:.4f}"                if self.roe                is not None else "  ROE: N/A")
        print(f"  Endividamento:      {self.endividamento:.4f}"      if self.endividamento      is not None else "  Endividamento: N/A")
        print("-" * 45)


class Empresa:
    def __init__(self, nome, cnpj):
        self.nome           = nome
        self.cnpj           = cnpj
        self.historico_anos = []

    def adicionar_ano(self, demonstracao):
        self.historico_anos.append(demonstracao)

    def exibir_historico(self):
        if not self.historico_anos:
            print("\nNenhum ano cadastrado ainda.")
            return
        print("\n" + "=" * 45)
        print(f"HISTÓRICO - {self.nome}")
        print("=" * 45)
        for dem in self.historico_anos:
            dem.exibir_resumo()

    # Análise Vertical e Horizontal - Victor Kenuy

    def _calcular_variacao(self, valor_novo, valor_velho):
        if valor_velho == 0:
            return None
        return ((valor_novo / valor_velho) - 1) * 100

    def _etiqueta(self, variacao):
        if variacao is None:
            return "N/A"
        if variacao >= 0:
            return f"[CRESCIMENTO] +{variacao:.2f}%"
        else:
            return f"[QUEDA] {variacao:.2f}%"

    def relatorio_geral(self):
        if len(self.historico_anos) < 2:
            print("\nÉ necessário ter pelo menos 2 anos cadastrados para o relatório geral.")
            return

        print("\n" + "=" * 45)
        print(f"RELATÓRIO GERAL - {self.nome}")
        print("=" * 45)

        for i in range(1, len(self.historico_anos)):
            ano_velho = self.historico_anos[i - 1]
            ano_novo  = self.historico_anos[i]

            print(f"\n  Comparando {ano_velho.ano} → {ano_novo.ano}")
            print("  " + "-" * 41)

            campos = [
                ("Lucro Líquido",      ano_velho.lucro_liquido,      ano_novo.lucro_liquido),
                ("Receita Líquida",    ano_velho.receita_liquida,    ano_novo.receita_liquida),
                ("Ativo Circulante",   ano_velho.ativo_circulante,   ano_novo.ativo_circulante),
                ("Passivo Circulante", ano_velho.passivo_circulante, ano_novo.passivo_circulante),
                ("Patrimônio Líquido", ano_velho.patrimonio_liquido, ano_novo.patrimonio_liquido),
                ("Liquidez Corrente",  ano_velho.liquidez_corrente,  ano_novo.liquidez_corrente),
                ("Margem Líquida",     ano_velho.margem_liquida,     ano_novo.margem_liquida),
                ("ROE",                ano_velho.roe,                ano_novo.roe),
                ("Endividamento",      ano_velho.endividamento,      ano_novo.endividamento),
            ]

            for nome, v_velho, v_novo in campos:
                if v_velho is None or v_novo is None:
                    print(f"  {nome:<22} N/A")
                    continue
                variacao = self._calcular_variacao(v_novo, v_velho)
                print(f"  {nome:<22} {self._etiqueta(variacao)}")

        print("\n" + "=" * 45)

# INGRESSO DE DADOS - Jean Soares
# Parte da coleta/validação de dados:

def ler_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("AVISO: Digite um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Erro! Valor inválido. Digite apenas números (ex: 150000).")

def coletar_dados(empresa):
    while True:
        print("\n" + "=" * 45)
        print("INSERÇÃO DE DADOS - BALANÇO PATRIMONIAL")
        print("=" * 45)

        ano = input("Ano de referência (ex: 2025): ").strip()

        print("\nATIVOS:")
        ativo_circulante = ler_valor("  Ativo Circulante:       R$ ")
        estoques         = ler_valor("  Estoques:               R$ ")
        ativo_nao_circ   = ler_valor("  Ativo Não Circulante:   R$ ")
        ativo_total      = ativo_circulante + ativo_nao_circ
        print(f"  -> Ativo Total: R$ {ativo_total:,.2f}")

        print("\nPASSIVOS:")
        passivo_circulante = ler_valor("  Passivo Circulante:     R$ ")
        passivo_nao_circ   = ler_valor("  Passivo Não Circulante: R$ ")
        passivo_total      = passivo_circulante + passivo_nao_circ
        print(f"  -> Passivo Total: R$ {passivo_total:,.2f}")

        print("\nPATRIMÔNIO LÍQUIDO:")
        patrimonio_liquido = ler_valor("  Patrimônio Líquido:     R$ ")

        print("\nDRE:")
        receita_liquida = ler_valor("  Receita Líquida:        R$ ")
        lucro_liquido   = ler_valor("  Lucro Líquido:          R$ ")

        soma_passivo_pl = passivo_total + patrimonio_liquido

        if ativo_total != soma_passivo_pl:
            print("\n" + "!" * 45)
            print("ERRO FATAL: Balanço não fecha!")
            print(f"  Ativo Total:        R$ {ativo_total:,.2f}")
            print(f"  Passivo Total + PL: R$ {soma_passivo_pl:,.2f}")
            print("Verifique os valores e tente novamente.")
            print("!" * 45)
            continue

        demonstracao = DemonstracaoAnual(
            ano, ativo_circulante, estoques, ativo_nao_circ,
            passivo_circulante, passivo_nao_circ, passivo_total,
            patrimonio_liquido, receita_liquida, lucro_liquido
        )
        empresa.adicionar_ano(demonstracao)
        print(f"\nOk! Balanço validado! Ano {ano} salvo no histórico.")
        return


# Parte do menu interativo:

def exibir_menu(empresa):
    print("\n" + "=" * 45)
    print("DASHBOARD FINANCEIRO - SISTEMA CONTÁBIL")
    print(f"Empresa: {empresa.nome}")
    print("=" * 45)
    print("(1) Inserir dados de um ano")
    print("(2) Ver histórico da empresa")
    print("(3) Ver relatório geral")
    print("(4) Sair")
    print("=" * 45)

def cadastrar_empresa():
    print("\n" + "=" * 45)
    print("BEM-VINDO AO DASHBOARD FINANCEIRO!")
    print("=" * 45)
    nome = input("Nome da empresa: ").strip()
    cnpj = input("CNPJ da empresa: ").strip()
    return Empresa(nome, cnpj)

def boas_vindas():
    empresa = cadastrar_empresa()
    print(f"\nEmpresa '{empresa.nome}' cadastrada com sucesso!")

    while True:
        exibir_menu(empresa)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            coletar_dados(empresa)
        elif opcao == "2":
            empresa.exibir_historico()
        elif opcao == "3":
            empresa.relatorio_geral()
        elif opcao == "4":
            print("\nAté mais! Encerrando o sistema...")
            break
        else:
            print("\nErro! Opção inválida! Tente novamente.")

boas_vindas()
