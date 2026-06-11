class Menu:

    def exibir_principal(self):
        print("\n=============================")
        print("       ERP EDUCACIONAL")
        print("=============================")
        print("[1] Cadastrar Professor")
        print("[2] Cadastrar Aluno")
        print("[3] Alocar Aula")
        print("[4] Lançar Notas")
        print("[5] Gerar Relatório")
        print("[0] Encerrar Programa")
        while True:
            opcao = input("=> ").strip()
            if opcao in ["0","1","2","3","4","5"]:
                return opcao
            print("[ERRO] Opção inválida!")

    def coletar_dados_professor(self):
        nome  = input("Nome do professor: ").strip().title()
        while True:
            try:
                carga = int(input("Carga horaria maxima (h): "))
                if 1 <= carga <= 40:
                    return nome, carga
                print("[ERRO] Entre 1 e 40h")
            except ValueError:
                print("[ERRO] Digite penas números!")

    def coletar_dados_aluno(self):
        nome = input("Nome do aluno: ").strip().title()
        matricula = input("Matricula: ").strip()
        return nome, matricula

    def coletar_nota(self, nome):
        while True:
            try:
                v = float(input(f"  {nome} (0-10): "))
                if 0 <= v <= 10:
                    return v
                print("[ERRO] Nota fora do intervalo!")
            except ValueError:
                print("[ERRO] Digite um número!")

    def fluxo_alocacao(self, motor):
        print("\n--- Alocar Aula ---")
        nome_prof  = input("Nome do professor: ").strip().title()
        cod_turma  = input("Código da turma  : ").strip()
        cod_disc   = input("Código da disciplina: ").strip()
        slot       = input("Slot (ex: SEG_MANHA): ").strip().upper()
        horas      = int(input("Horas da disciplina: "))
        sucesso, mensagem = motor.alocar(nome_prof, cod_turma, cod_disc, slot, horas)
        print(f"{'===' if sucesso else '[ERRO]'} {mensagem} {'===' if sucesso else '[ERRO]'}")

    def fluxo_notas(self, diario):
        print("\n--- Lançar Notas ---")
        matricula = input("Matrícula do aluno: ").strip()
        disciplina = input("Disciplina: ").strip()
        av1 = self.coletar_nota("AV1")
        av2 = self.coletar_nota("AV2")
        av3 = self.coletar_nota("AV3")
        sucesso, mensagem = diario.lancar_notas(matricula, disciplina, av1, av2, av3)
        print(f"{'===' if sucesso else '[ERRO]'} {mensagem} {'===' if sucesso else '[ERROR]'}")



     



  
