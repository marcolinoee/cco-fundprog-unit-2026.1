from entidades_poo import Professor, Turma, Disciplina, Aluno


def calcular_media_parcial(av1, av2, av3):
    return (av1 * 0.3) + (av2 * 0.3) + (av3 * 0.4)


def determinar_status(media_parcial, nota_final=None):
    if media_parcial >= 7.0:
        return "Aprovado Direto", media_parcial
    elif media_parcial < 4.0:
        return "Reprovado Direto", media_parcial
    else:
        if nota_final is not None:
            media_final = (media_parcial + nota_final) / 2
            if media_final >= 5.0:
                return "Aprovado na Final", media_final
            else:
                return "Reprovado na Final", media_final
        else:
            return "Prova Final", media_parcial

def adicionar_aluno(alunos,  aluno):
        alunos.append(aluno)


def processar_diario(diario):
    resultados = []
    for i in range(len(diario)):
        aluno = diario[i]
        nome = aluno[0]
        notas = []
        for j in range(1, 4):
            notas.append(float(aluno[j]))
        av1, av2, av3 = notas[0], notas[1], notas[2]
        nota_final = float(aluno[4]) if len(aluno) > 4 else None
        media_parcial = calcular_media_parcial(av1, av2, av3)
        status, media_exibir = determinar_status(media_parcial, nota_final)
        resultados.append({
            "nome": nome,
            "av1": av1,
            "av2": av2,
            "av3": av3,
            "media_parcial": media_parcial,
            "nota_final": nota_final,
            "media_exibir": media_exibir,
            "status": status
        })
    return resultados


def gerar_relatorio_ascii(resultados):
    print("\n" + "=" * 95)
    print(" " * 30 + "DIÁRIO DE CLASSE - RELATÓRIO DE NOTAS")
    print("=" * 95)
    print(f"{'Aluno':<15} | {'AV1':^6} | {'AV2':^6} | {'AV3':^6} | {'MP':^6} | {'PF':^6} | {'MF':^6} | {'Status':<20}")
    print("-" * 95)
    for aluno in resultados:
        pf_str = f"{aluno['nota_final']:.1f}" if aluno['nota_final'] is not None else "  -  "
        if aluno['nota_final'] is not None:
            mf_str = f"{aluno['media_exibir']:.1f}"
        elif aluno['status'] == "Prova Final":
            mf_str = "  -  "
        else:
            mf_str = f"{aluno['media_exibir']:.1f}"
        print(f"{aluno['nome']:<15} | {aluno['av1']:^6.1f} | {aluno['av2']:^6.1f} | "
              f"{aluno['av3']:^6.1f} | {aluno['media_parcial']:^6.1f} | {pf_str:^6} | "
              f"{mf_str:^6} | {aluno['status']:<20}")
    print("=" * 95)
    print("\nLegenda: MP = Média Parcial | PF = Prova Final | MF = Média Final")
    print("Pesos: AV1 (30%) | AV2 (30%) | AV3 (40%)")
    print("Aprovação: MP >= 7.0 (Direto) | MP < 4.0 (Reprovado) | 4.0 <= MP < 7.0 (Prova Final)")
    print()


def lancar_notas():
    diario = []
    print("\n" + "=" * 50)
    print("       LANÇAMENTO DE NOTAS - DIÁRIO DE CLASSE")
    print("=" * 50)
    while True:
        nome = input("\nNome do aluno (ou 'sair' para finalizar): ").strip()
        if nome.lower() == 'sair':
            break
        try:
            av1 = float(input(f"  AV1 de {nome.title()}: ").strip())
            av2 = float(input(f"  AV2 de {nome.title()}: ").strip())
            av3 = float(input(f"  AV3 de {nome.title()}: ").strip())
            mp = calcular_media_parcial(av1, av2, av3)
            if 4.0 <= mp < 7.0:
                resposta = input(f"  {nome.title()} precisa de Prova Final (MP={mp:.1f}). Lançar nota? (s/n): ").strip().lower()
                if resposta == 's':
                    pf = float(input("  Nota da Prova Final: ").strip())
                    diario.append([nome, av1, av2, av3, pf])
                else:
                    diario.append([nome, av1, av2, av3])
            else:
                diario.append([nome, av1, av2, av3])
            print(f"  ✓ {nome.title()} adicionado(a) ao diário!")
            break
        except ValueError:
            print("  ✗ Erro: Digite apenas números para as notas.")
    return diario


def turma_para_diario(turma_obj, notas_por_nome):
    diario = []
    for aluno in turma_obj.alunos:
        nome = aluno.nome
        if nome not in notas_por_nome:
            continue
        pacote = notas_por_nome[nome]
        if len(pacote) == 3:
            av1, av2, av3 = pacote
            diario.append([nome, av1, av2, av3])
        elif len(pacote) == 4:
            av1, av2, av3, pf = pacote
            diario.append([nome, av1, av2, av3, pf])
    return diario


def lancar_notas_para_turma(turma_obj):
    diario = []
    print("\n" + "=" * 60)
    print(f"   LANÇAR NOTAS PARA A TURMA {turma_obj.codigo}")
    print("=" * 60)
    if not getattr(turma_obj, "alunos", []):
        print("Nenhum aluno cadastrado na turma.")
        return diario

    print("\nAlunos na turma:")
    for idx, aluno in enumerate(turma_obj.alunos, start=1):
        print(f"  {idx:02d}. {aluno.nome}")

    print("\nDigite as notas para cada aluno (ou deixe em branco para pular).")
    for aluno in turma_obj.alunos:
        nome = aluno.nome
        try:
            entrada = input(f"\nNotas de {nome} (formato: av1, av2, av3, pf) ou ENTER para pular: ").strip()
            if not entrada:
                continue
            partes = [p.strip() for p in entrada.split(",")]
            if len(partes) not in (3, 4):
                print("  ✗ Formato inválido. Use: av1, av2, av3 ou av1, av2, av3, pf")
                continue
            av1 = float(partes[0]); av2 = float(partes[1]); av3 = float(partes[2])
            if len(partes) == 4:
                pf = float(partes[3])
                diario.append([nome, av1, av2, av3, pf])
            else:
                mp = calcular_media_parcial(av1, av2, av3)
                if 4.0 <= mp < 7.0:
                    resp = input(f"  {nome} precisa de PF (MP={mp:.1f}). Lançar PF agora? (s/n): ").strip().lower()
                    if resp == "s":
                        pf = float(input("  Nota da Prova Final: ").strip())
                        diario.append([nome, av1, av2, av3, pf])
                    else:
                        diario.append([nome, av1, av2, av3])
                else:
                    diario.append([nome, av1, av2, av3])
            print(f"  ✓ Notas registradas para {nome}.")
        except ValueError:
            print("  ✗ Erro: digite apenas números nas notas.")
    return diario


def relatorio_da_turma(turma_obj, notas_por_nome):
    diario = turma_para_diario(turma_obj, notas_por_nome)
    resultados = processar_diario(diario)
    gerar_relatorio_ascii(resultados)


    # Ambiente de exemplo
    prof = Professor("Fernanda Souza")
    disc = Disciplina("Algoritmos e Programação", "AP101")
    turma = Turma("AP101-2026.1", prof, disc)

    for (nome, mat) in [
        ("Maria", "2026001"),
        ("João", "2026002"),
        ("Ana", "2026003"),
        ("Pedro", "2026004"),
        ("Carla", "2026005"),
        ("Lucas", "2026006"),
    ]:
        turma.adicionar_aluno(Aluno(nome, mat))

    # Diário de teste (matriz, não dicionário!)
    diario_teste = [
        ["Maria", 5.0, 6.0, 4.0, 6.5],
        ["João",  8.0, 7.5, 9.0],
        ["Ana",   3.0, 2.5, 3.5],
        ["Pedro", 5.5, 6.0, 5.0, 4.0],
        ["Carla", 7.0, 7.0, 7.0],
        ["Lucas", 4.5, 5.0, 4.0],
    ]
    
    while True:
        print("\n" + "=" * 70)
        print("        SISTEMA DE DIÁRIO DE CLASSE - MENU PRINCIPAL")
        print("=" * 70)
        print("1 - Usar diário de teste (dados pré-definidos)")
        print("2 - Lançar notas manualmente (sem Turma POO)")
        print("3 - Lançar notas para alunos da Turma (POO)")
        print("4 - Gerar relatório da Turma a partir de dicionário de notas")
        print("0 - Sair")

        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            resultados = processar_diario(diario_teste)
            gerar_relatorio_ascii(resultados)

        elif opcao == "2":
            diario = lancar_notas()
            if not diario:
                print("\nNenhum aluno lançado.")
            else:
                resultados = processar_diario(diario)
                gerar_relatorio_ascii(resultados)

        elif opcao == "3":
            diario_turma = lancar_notas_para_turma(turma)
            if not diario_turma:
                print("\nNenhuma nota registrada para a Turma.")
            else:
                resultados = processar_diario(diario_turma)
                gerar_relatorio_ascii(resultados)

        elif opcao == "4":
            notas = {
                "Maria": (5.0, 6.0, 4.0, 6.5),
                "João":  (8.0, 7.5, 9.0),
                "Ana":   (3.0, 2.5, 3.5),
                "Pedro": (5.5, 6.0, 5.0, 4.0),
                "Carla": (7.0, 7.0, 7.0),
                "Lucas": (4.5, 5.0, 4.0),
            }
            diario = turma_para_diario(turma, notas)
            if not diario:
                print("\nNenhum dado gerado a partir das notas informadas.")
            else:
                resultados = processar_diario(diario)
                gerar_relatorio_ascii(resultados)

        elif opcao == "0":
            print("\nEncerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")

        
