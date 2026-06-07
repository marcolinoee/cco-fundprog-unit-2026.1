nomes = []
investimentos = []
taxas = []
fluxos_todos = []

rodando = True

print("=" * 55)
print("  BEM-VINDO AO MOTOR DO PORTFÓLIO DE INVESTIMENTOS")
print("=" * 55)

while rodando:

    print()
    print("╔" + "═" * 48 + "╗")
    print("║   MENU PRINCIPAL                               ║")
    print("╠" + "═" * 48 + "╣")
    print("║  1. Cadastrar projeto                          ║")
    print("║  2. Listar projetos                            ║")
    print("║  3. Análise financeira (VPL, Payback, IL)      ║")
    print("║  4. Otimização de portfólio                    ║")
    print("║  5. Relatório de risco (cenário pessimista)    ║")
    print("║  0. Sair                                       ║")
    print("╚" + "═" * 48 + "╝")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":

        print("\n" + "─" * 50)
        print("  CADASTRO DE PROJETO")
        print("─" * 50)

        nome = input("Nome do projeto: ").strip()
        while nome == "":
            print("  O nome não pode ser vazio.")
            nome = input("Nome do projeto: ").strip()

        investimento_valido = False
        while not investimento_valido:
            try:
                investimento = float(input("Investimento inicial (R$): "))
                if investimento < 0.01:
                    print("  Valor mínimo: R$ 0.01")
                else:
                    investimento_valido = True
            except ValueError:
                print("  Entrada inválida. Digite um número.")

        taxa_valida = False
        while not taxa_valida:
            try:
                taxa = float(input("Taxa de desconto anual (ex: 0.10 para 10%): "))
                if taxa < 0:
                    print("  A taxa não pode ser negativa.")
                else:
                    taxa_valida = True
            except ValueError:
                print("  Entrada inválida. Digite um número.")

        anos_valido = False
        while not anos_valido:
            try:
                anos = int(input("Número de anos de fluxo (5 a 10): "))
                if anos < 5:
                    print("  Mínimo: 5 anos.")
                elif anos > 10:
                    print("  Máximo: 10 anos.")
                else:
                    anos_valido = True
            except ValueError:
                print("  Entrada inválida. Digite um número inteiro.")

        print(f"\nInforme o fluxo de caixa para cada um dos {anos} anos:")
        fluxos_projeto = []

        for ano in range(1, anos + 1):
            fluxo_valido = False
            while not fluxo_valido:
                try:
                    fc = float(input(f"  Ano {ano}: R$ "))
                    fluxo_valido = True
                except ValueError:
                    print("  Entrada inválida. Digite um número.")
            fluxos_projeto.append(fc)

        nomes.append(nome)
        investimentos.append(investimento)
        taxas.append(taxa)
        fluxos_todos.append(fluxos_projeto)

        print(f"\n  Projeto '{nome}' cadastrado com sucesso!")

    elif opcao == "2":

        if len(nomes) == 0:
            print("\n  Nenhum projeto cadastrado.")
        else:
            print("\n  PROJETOS CADASTRADOS")
            print("─" * 50)
            for i in range(len(nomes)):
                anos_projeto = len(fluxos_todos[i])
                print(f"  [{i + 1}] {nomes[i]}  —  R$ {investimentos[i]:,.2f}  —  {anos_projeto} anos")
            print("─" * 50)

    elif opcao == "3":

        if len(nomes) == 0:
            print("\n  Nenhum projeto cadastrado.")
        else:
            print("\n" + "═" * 70)
            print("  ANÁLISE FINANCEIRA DOS PROJETOS")
            print("═" * 70)

            total_investimento = 0
            total_vpl = 0

            for i in range(len(nomes)):
                fluxos  = fluxos_todos[i]
                invest  = investimentos[i]
                taxa    = taxas[i]

                vpl = -invest
                for t in range(len(fluxos)):
                    vpl += fluxos[t] / (1 + taxa) ** (t + 1)

                acumulado = 0
                payback_simples = None
                for t in range(len(fluxos)):
                    acumulado += fluxos[t]
                    if acumulado >= invest:
                        excesso = acumulado - invest
                        payback_simples = (t + 1) - excesso / fluxos[t]
                        break

                acumulado_desc = 0
                payback_desc = None
                for t in range(len(fluxos)):
                    fc_desc = fluxos[t] / (1 + taxa) ** (t + 1)
                    acumulado_desc += fc_desc
                    if acumulado_desc >= invest:
                        excesso_desc = acumulado_desc - invest
                        payback_desc = (t + 1) - excesso_desc / fc_desc
                        break

                soma_vp = 0
                for t in range(len(fluxos)):
                    soma_vp += fluxos[t] / (1 + taxa) ** (t + 1)
                il = soma_vp / invest

                total_investimento += invest
                total_vpl += vpl

                if vpl > 0 and il >= 1:
                    decisao = "VIÁVEL"
                    simbolo = "✔"
                elif vpl == 0:
                    decisao = "NEUTRO"
                    simbolo = "~"
                else:
                    decisao = "NÃO VIÁVEL"
                    simbolo = "✘"

                if payback_simples is not None:
                    pbs_str = f"{payback_simples:.1f} anos"
                else:
                    pbs_str = "Não recupera"

                if payback_desc is not None:
                    pbd_str = f"{payback_desc:.1f} anos"
                else:
                    pbd_str = "Não recupera"

                print(f"\n  [{simbolo}] {nomes[i]}  (taxa={taxa * 100:.1f}%)")
                print(f"      Investimento inicial : R$ {invest:>15,.2f}")
                print(f"      VPL                  : R$ {vpl:>15,.2f}")
                print(f"      Payback Simples      : {pbs_str}")
                print(f"      Payback Descontado   : {pbd_str}")
                print(f"      Índice Lucratividade : {il:.4f}")
                print(f"      Decisão              : {decisao}")

            print("\n" + "─" * 70)
            print(f"  Total investido  : R$ {total_investimento:>15,.2f}")
            print(f"  VPL do portfólio : R$ {total_vpl:>15,.2f}")
            print("═" * 70)

    elif opcao == "4":

        if len(nomes) == 0:
            print("\n  Nenhum projeto cadastrado.")
        else:
            print("\n" + "═" * 70)
            print("  MOTOR DE OTIMIZAÇÃO DE PORTFÓLIO")
            print("═" * 70)

            orcamento_valido = False
            while not orcamento_valido:
                try:
                    orcamento = float(input("\nInforme o orçamento global disponível (R$): "))
                    if orcamento < 0.01:
                        print("  Valor mínimo: R$ 0.01")
                    else:
                        orcamento_valido = True
                except ValueError:
                    print("  Entrada inválida. Digite um número.")

            vpls_candidatos    = []
            indices_candidatos = []

            for i in range(len(nomes)):
                fluxos = fluxos_todos[i]
                invest = investimentos[i]
                taxa   = taxas[i]

                vpl = -invest
                for t in range(len(fluxos)):
                    vpl += fluxos[t] / (1 + taxa) ** (t + 1)

                if vpl > 0:
                    indices_candidatos.append(i)
                    vpls_candidatos.append(vpl)

            if len(indices_candidatos) == 0:
                print("\n  Nenhum projeto com VPL positivo para otimizar.")
            else:
                n = len(indices_candidatos)
                melhor_vpl    = 0
                melhor_mascara = 0

                if n <= 15:
                    print(f"\n  Analisando {2**n} combinações possíveis...")

                    for mascara in range(1, 2 ** n):
                        custo_combo = 0
                        vpl_combo   = 0

                        for bit in range(n):
                            if mascara & (1 << bit):
                                idx = indices_candidatos[bit]
                                custo_combo += investimentos[idx]
                                vpl_combo   += vpls_candidatos[bit]

                        if custo_combo <= orcamento and vpl_combo > melhor_vpl:
                            melhor_vpl     = vpl_combo
                            melhor_mascara = mascara

                    aprovados = []
                    for bit in range(n):
                        if melhor_mascara & (1 << bit):
                            aprovados.append(indices_candidatos[bit])

                else:
                    print(f"\n  Usando estratégia gulosa para {n} projetos...")

                    ordem = list(range(n))
                    for a in range(n):
                        for b in range(a + 1, n):
                            ia = indices_candidatos[ordem[a]]
                            ib = indices_candidatos[ordem[b]]
                            ratio_a = vpls_candidatos[ordem[a]] / investimentos[ia]
                            ratio_b = vpls_candidatos[ordem[b]] / investimentos[ib]
                            if ratio_b > ratio_a:
                                ordem[a], ordem[b] = ordem[b], ordem[a]

                    restante = orcamento
                    aprovados = []
                    j = 0
                    while j < n and restante > 0:
                        idx = indices_candidatos[ordem[j]]
                        if investimentos[idx] <= restante:
                            aprovados.append(idx)
                            restante    -= investimentos[idx]
                            melhor_vpl  += vpls_candidatos[ordem[j]]
                        j += 1

                custo_total = 0
                for idx in aprovados:
                    custo_total += investimentos[idx]

                print("\n  RESULTADO DA OTIMIZAÇÃO")
                print("─" * 70)

                for i in range(len(nomes)):
                    fluxos = fluxos_todos[i]
                    invest = investimentos[i]
                    taxa   = taxas[i]

                    vpl = -invest
                    for t in range(len(fluxos)):
                        vpl += fluxos[t] / (1 + taxa) ** (t + 1)

                    if i in aprovados:
                        status = "APROVADO"
                    elif vpl <= 0:
                        status = "VPL negativo"
                    else:
                        status = "Orçamento insuficiente"

                    print(f"  {status:<25} {nomes[i]:<30} R$ {invest:>12,.2f}")

                print("─" * 70)
                print(f"  Orçamento disponível  : R$ {orcamento:>12,.2f}")
                print(f"  Orçamento utilizado   : R$ {custo_total:>12,.2f}")
                print(f"  Saldo remanescente    : R$ {orcamento - custo_total:>12,.2f}")
                print(f"  VPL total aprovado    : R$ {melhor_vpl:>12,.2f}")
                print("═" * 70)

    elif opcao == "5":

        if len(nomes) == 0:
            print("\n  Nenhum projeto cadastrado.")
        else:
            print("\n" + "═" * 70)
            print("  RELATÓRIO DE RISCO — Cenário pessimista (fluxos −10%)")
            print("═" * 70)

            mudancas = 0

            for i in range(len(nomes)):
                fluxos = fluxos_todos[i]
                invest = investimentos[i]
                taxa   = taxas[i]

                vpl_base = -invest
                for t in range(len(fluxos)):
                    vpl_base += fluxos[t] / (1 + taxa) ** (t + 1)

                fluxos_pess = []
                for fc in fluxos:
                    fluxos_pess.append(fc * 0.9)

                vpl_pess = -invest
                for t in range(len(fluxos_pess)):
                    vpl_pess += fluxos_pess[t] / (1 + taxa) ** (t + 1)

                impacto = vpl_pess - vpl_base

                if vpl_base != 0:
                    variacao = impacto / abs(vpl_base) * 100
                else:
                    variacao = 0

                if vpl_base >= 0 and vpl_pess >= 0:
                    status = "Mantém viabilidade"
                elif vpl_base >= 0 and vpl_pess < 0:
                    status = "TORNA-SE INVIÁVEL"
                    mudancas += 1
                elif vpl_base < 0 and vpl_pess < 0:
                    status = "Já era inviável"
                else:
                    status = "Melhora no pessimista"

                print(f"\n  Projeto : {nomes[i]}")
                print(f"    VPL base       : R$ {vpl_base:>12,.2f}")
                print(f"    VPL pessimista : R$ {vpl_pess:>12,.2f}")
                print(f"    Impacto        : R$ {impacto:>12,.2f}  ({variacao:+.1f}%)")
                print(f"    Status         : {status}")

            print("\n" + "─" * 70)
            if mudancas > 0:
                print(f"  ATENÇÃO: {mudancas} projeto(s) tornam-se inviáveis no cenário pessimista!")
            else:
                print("  Portfólio resiliente: nenhum projeto viável torna-se inviável.")
            print("═" * 70)

    elif opcao == "0":
        print("\nEncerrando o simulador. Até logo!")
        rodando = False

    else:
        print("\n  Opção inválida. Tente novamente.")
