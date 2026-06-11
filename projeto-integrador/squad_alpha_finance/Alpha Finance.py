class ProjetoInvestimento:

    def _init_(self, nome, investimento, taxa, fluxos):
        self.nome         = nome
        self.investimento = investimento
        self.taxa         = taxa
        self.fluxos       = fluxos
        self.vpl          = 0.0
        self.il           = 0.0

    def calcular_vpl(self):
        resultado = -self.investimento
        for t in range(len(self.fluxos)):
            resultado += self.fluxos[t] / (1 + self.taxa) ** (t + 1)
        self.vpl = resultado

    def calcular_il(self):
        soma_vp = 0.0
        for t in range(len(self.fluxos)):
            soma_vp += self.fluxos[t] / (1 + self.taxa) ** (t + 1)
        self.il = soma_vp / self.investimento

    def calcular_payback_simples(self):
        acumulado = 0.0
        for t in range(len(self.fluxos)):
            acumulado += self.fluxos[t]
            if acumulado >= self.investimento:
                excesso = acumulado - self.investimento
                return (t + 1) - excesso / self.fluxos[t]
        return None

    def calcular_payback_descontado(self):
        acumulado = 0.0
        for t in range(len(self.fluxos)):
            fc_desc = self.fluxos[t] / (1 + self.taxa) ** (t + 1)
            acumulado += fc_desc
            if acumulado >= self.investimento:
                excesso = acumulado - self.investimento
                return (t + 1) - excesso / fc_desc
        return None


projetos = []


def cadastrar_projeto():
    print("\n" + "-" * 50)
    print("  CADASTRO DE PROJETO")
    print("-" * 50)

    nome = input("Nome do projeto: ").strip()
    while nome == "":
        print("  O nome nao pode ser vazio.")
        nome = input("Nome do projeto: ").strip()

    investimento_valido = False
    while not investimento_valido:
        try:
            investimento = float(input("Investimento inicial (R$): "))
            if investimento < 0.01:
                print("  Valor minimo: R$ 0.01")
            else:
                investimento_valido = True
        except ValueError:
            print("  Entrada invalida. Digite um numero.")

    taxa_valida = False
    while not taxa_valida:
        try:
            taxa = float(input("Taxa de desconto anual (ex: 0.10 para 10%): "))
            if taxa < 0:
                print("  A taxa nao pode ser negativa.")
            else:
                taxa_valida = True
        except ValueError:
            print("  Entrada invalida. Digite um numero.")

    anos_valido = False
    while not anos_valido:
        try:
            anos = int(input("Numero de anos de fluxo (5 a 10): "))
            if anos < 5:
                print("  Minimo: 5 anos.")
            elif anos > 10:
                print("  Maximo: 10 anos.")
            else:
                anos_valido = True
        except ValueError:
            print("  Entrada invalida. Digite um numero inteiro.")

    print(f"\nInforme o fluxo de caixa para cada um dos {anos} anos:")
    fluxos = []
    for ano in range(1, anos + 1):
        fluxo_valido = False
        while not fluxo_valido:
            try:
                fc = float(input(f"  Ano {ano}: R$ "))
                fluxo_valido = True
            except ValueError:
                print("  Entrada invalida. Digite um numero.")
        fluxos.append(fc)

    projeto = ProjetoInvestimento(nome, investimento, taxa, fluxos)
    projeto.calcular_vpl()
    projeto.calcular_il()
    projetos.append(projeto)

    print(f"\n  Projeto '{nome}' cadastrado com sucesso!")


def listar_projetos():
    if len(projetos) == 0:
        print("\n  Nenhum projeto cadastrado.")
        return

    print("\n  PROJETOS CADASTRADOS")
    print("-" * 50)
    for i in range(len(projetos)):
        p = projetos[i]
        print(f"  [{i + 1}] {p.nome}  -  R$ {p.investimento:,.2f}  -  {len(p.fluxos)} anos")
    print("-" * 50)


def analise_financeira():
    if len(projetos) == 0:
        print("\n  Nenhum projeto cadastrado.")
        return

    print("\n" + "=" * 70)
    print("  ANALISE FINANCEIRA DOS PROJETOS")
    print("=" * 70)

    total_investimento = 0.0
    total_vpl          = 0.0

    for i in range(len(projetos)):
        p = projetos[i]

        p.calcular_vpl()
        p.calcular_il()
        pbs = p.calcular_payback_simples()
        pbd = p.calcular_payback_descontado()

        total_investimento += p.investimento
        total_vpl          += p.vpl

        if p.vpl > 0 and p.il >= 1:
            decisao = "VIAVEL"
            simbolo = "+"
        elif p.vpl == 0:
            decisao = "NEUTRO"
            simbolo = "~"
        else:
            decisao = "NAO VIAVEL"
            simbolo = "X"

        if pbs is not None:
            pbs_str = f"{pbs:.1f} anos"
        else:
            pbs_str = "Nao recupera"

        if pbd is not None:
            pbd_str = f"{pbd:.1f} anos"
        else:
            pbd_str = "Nao recupera"

        print(f"\n  [{simbolo}] {p.nome}  (taxa={p.taxa * 100:.1f}%)")
        print(f"      Investimento inicial : R$ {p.investimento:>15,.2f}")
        print(f"      VPL                  : R$ {p.vpl:>15,.2f}")
        print(f"      Payback Simples      : {pbs_str}")
        print(f"      Payback Descontado   : {pbd_str}")
        print(f"      Indice Lucratividade : {p.il:.4f}")
        print(f"      Decisao              : {decisao}")

    print("\n" + "-" * 70)
    print(f"  Total investido  : R$ {total_investimento:>15,.2f}")
    print(f"  VPL do portfolio : R$ {total_vpl:>15,.2f}")
    print("=" * 70)


def otimizar_portfolio():
    if len(projetos) == 0:
        print("\n  Nenhum projeto cadastrado.")
        return

    print("\n" + "=" * 70)
    print("  OTIMIZACAO DE PORTFOLIO  (Algoritmo Guloso)")
    print("=" * 70)

    orcamento_valido = False
    while not orcamento_valido:
        try:
            orcamento = float(input("\nInforme o orcamento global disponivel (R$): "))
            if orcamento < 0.01:
                print("  Valor minimo: R$ 0.01")
            else:
                orcamento_valido = True
        except ValueError:
            print("  Entrada invalida. Digite um numero.")

    candidatos = []
    for i in range(len(projetos)):
        p = projetos[i]
        p.calcular_vpl()
        p.calcular_il()
        if p.vpl > 0:
            candidatos.append(p)

    if len(candidatos) == 0:
        print("\n  Nenhum projeto com VPL positivo para otimizar.")
        return

    candidatos.sort(key=lambda p: p.il, reverse=True)

    aprovados = []
    restante  = orcamento

    for i in range(len(candidatos)):
        p = candidatos[i]
        if p.investimento <= restante:
            aprovados.append(p)
            restante -= p.investimento

    custo_total = 0.0
    vpl_total   = 0.0
    for i in range(len(aprovados)):
        custo_total += aprovados[i].investimento
        vpl_total   += aprovados[i].vpl

    print("\n  RESULTADO DA OTIMIZACAO")
    print("-" * 70)

    for i in range(len(projetos)):
        p = projetos[i]
        esta_aprovado = False
        for j in range(len(aprovados)):
            if aprovados[j] is p:
                esta_aprovado = True
                break

        if esta_aprovado:
            status = "APROVADO"
        elif p.vpl <= 0:
            status = "VPL negativo"
        else:
            status = "Orcamento insuficiente"

        print(f"  {status:<25} {p.nome:<30} R$ {p.investimento:>12,.2f}")

    print("-" * 70)
    print(f"  Orcamento disponivel  : R$ {orcamento:>12,.2f}")
    print(f"  Orcamento utilizado   : R$ {custo_total:>12,.2f}")
    print(f"  Saldo remanescente    : R$ {orcamento - custo_total:>12,.2f}")
    print(f"  VPL total aprovado    : R$ {vpl_total:>12,.2f}")
    print("=" * 70)


def relatorio_risco():
    if len(projetos) == 0:
        print("\n  Nenhum projeto cadastrado.")
        return

    print("\n" + "=" * 70)
    print("  RELATORIO DE RISCO - Cenario pessimista (fluxos -10%)")
    print("=" * 70)

    mudancas = 0

    for i in range(len(projetos)):
        p = projetos[i]

        p.calcular_vpl()
        vpl_base = p.vpl

        fluxos_pess = []
        for t in range(len(p.fluxos)):
            fluxos_pess.append(p.fluxos[t] * 0.9)

        vpl_pess = -p.investimento
        for t in range(len(fluxos_pess)):
            vpl_pess += fluxos_pess[t] / (1 + p.taxa) ** (t + 1)

        impacto = vpl_pess - vpl_base

        if vpl_base != 0:
            variacao = impacto / abs(vpl_base) * 100
        else:
            variacao = 0.0

        if vpl_base >= 0 and vpl_pess >= 0:
            status = "Mantem viabilidade"
        elif vpl_base >= 0 and vpl_pess < 0:
            status = "TORNA-SE INVIAVEL"
            mudancas += 1
        elif vpl_base < 0 and vpl_pess < 0:
            status = "Ja era inviavel"
        else:
            status = "Melhora no pessimista"

        print(f"\n  Projeto : {p.nome}")
        print(f"    VPL base       : R$ {vpl_base:>12,.2f}")
        print(f"    VPL pessimista : R$ {vpl_pess:>12,.2f}")
        print(f"    Impacto        : R$ {impacto:>12,.2f}  ({variacao:+.1f}%)")
        print(f"    Status         : {status}")

    print("\n" + "-" * 70)
    if mudancas > 0:
        print(f"  ATENCAO: {mudancas} projeto(s) tornam-se inviaveis no cenario pessimista!")
    else:
        print("  Portfolio resiliente: nenhum projeto viavel torna-se inviavel.")
    print("=" * 70)


print("=" * 55)
print("  BEM-VINDO AO MOTOR DO PORTFOLIO DE INVESTIMENTOS")
print("=" * 55)

rodando = True

while rodando:

    print()
    print("+" + "=" * 48 + "+")
    print("|   MENU PRINCIPAL                               |")
    print("+" + "=" * 48 + "+")
    print("|  1. Cadastrar projeto                          |")
    print("|  2. Listar projetos                            |")
    print("|  3. Analise financeira (VPL, Payback, IL)      |")
    print("|  4. Otimizacao de portfolio                    |")
    print("|  5. Relatorio de risco (cenario pessimista)    |")
    print("|  0. Sair                                       |")
    print("+" + "=" * 48 + "+")

    opcao = input("\nEscolha uma opcao: ").strip()

    if opcao == "1":
        cadastrar_projeto()
    elif opcao == "2":
        listar_projetos()
    elif opcao == "3":
        analise_financeira()
    elif opcao == "4":
        otimizar_portfolio()
    elif opcao == "5":
        relatorio_risco()
    elif opcao == "0":
        print("\nEncerrando o simulador. Ate logo!")
        rodando = False
    else:
        print("\n  Opcao invalida. Tente novamente.")
