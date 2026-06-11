from entidades_poo import Professor, Disciplina, Turma

SLOTS_VALIDOS = [
    "SEG_MANHA", "SEG_NOITE",
    "TER_MANHA", "TER_NOITE",
    "QUA_MANHA", "QUA_NOITE",
    "QUI_MANHA", "QUI_NOITE",
    "SEX_MANHA", "SEX_NOITE",
]


class MotorAlocacao:
   

    def __init__(self):
        self.professores: list[Professor]  = []
        self.turmas:      list[Turma]      = []
        self.alocacoes:   list[dict]       = []

    def cadastrar_professor(self, professor: Professor) -> None:
        for prof in self.professores:
            if prof.nome == professor.nome:
                print(f"[ERRO] Prof. {professor.nome.title()} já está cadastrado.")
                return
        self.professores.append(professor)
        print(f"Prof. {professor.nome.title()} cadastrado com sucesso!")

    def cadastrar_turma(self, turma: Turma) -> None:
        for t in self.turmas:
            if t.codigo == turma.codigo:
                print(f"[ERRO] Turma {turma.codigo} já está cadastrada.")
                return
        self.turmas.append(turma)
        print(f"Turma {turma.codigo} cadastrada com sucesso!")

    def buscar_professor(self, nome: str) -> Professor | None:
        for prof in self.professores:
            if prof.nome == nome:
                return prof
        return None

    def buscar_turma(self, codigo: str) -> Turma | None:
        for turma in self.turmas:
            if turma.codigo == codigo:
                return turma
        return None

    def choque_professor(self, nome_prof: str, slot: str) -> bool:
        
        for alocacao in self.alocacoes:
            if alocacao["professor"] == nome_prof and alocacao["slot"] == slot:
                return True     
        return False            

    def choque_turma(self, cod_turma: str, slot: str) -> bool:
        
        for alocacao in self.alocacoes:
            if alocacao["turma"] == cod_turma and alocacao["slot"] == slot:
                return True
        return False

    def slot_valido(self, slot: str) -> bool:
        return slot in SLOTS_VALIDOS

    def alocar(
        self,
        nome_prof:  str,
        cod_turma:  str,
        disciplina: str,
        slot:       str,
        horas:      str
    ) -> tuple[bool, str]:
        
        
        if not self.slot_valido(slot):
            return False, (
                f"Slot '{slot}' inválido. "
                f"Slots aceitos: {', '.join(SLOTS_VALIDOS)}"
            )

        
        prof = self.buscar_professor(nome_prof)
        if prof is None:
            return False, (
                f"Professor '{nome_prof}' não encontrado. "
                f"Cadastre-o antes de alocar."
            )

        
        carga_valida = prof.adicionar_aula(slot)
        if not carga_valida:
            return False, (
                f"Prof. {nome_prof} atingiu o limite de "
                f"{prof.carga_max} aula(s). Alocação recusada."
            )

        # 5. Choque de professor?
        if self.choque_professor(nome_prof, slot):
            prof.remover_ultima_aula()          
            return False, (
                f"CHOQUE: Prof. {nome_prof} já possui aula "
                f"no slot '{slot}'."
            )

        # 6. Choque de turma?
        if self.choque_turma(cod_turma, slot):
            prof.remover_ultima_aula()          
            return False, (
                f"CHOQUE: Turma '{cod_turma}' já possui aula "
                f"no slot '{slot}'."
            )

        # Tudo ok — registra a alocação
        self.alocacoes.append({
            "professor":  nome_prof,
            "turma":      cod_turma,
            "disciplina": disciplina,
            "slot":       slot,
            "horas":      horas,
        })

        return True, (
            f"Alocação realizada: Prof. {nome_prof} | "
            f"Turma {cod_turma} | {disciplina} | {slot} | {horas}H"
        )

  

    def listar_alocacoes(self) -> None:
        if not self._alocacoes:
            print("\n[AVISO] Nenhuma aula alocada ainda.")
            return

        print("\n" + "=" * 70)
        print(" " * 20 + "GRADE DE ALOCAÇÕES")
        print("=" * 70)
        print(
            f"{'PROFESSOR':<20} {'TURMA':<12} "
            f"{'DISCIPLINA':<18} {'SLOT':<12}"
        )
        print("-" * 70)

        for alocacao in self._alocacoes:
            print(
                f"{alocacao['professor']:<20} {alocacao['turma']:<12} "
                f"{alocacao['disciplina']:<18} {alocacao['slot']:<12}"
            )
        print("=" * 70)
        print(f"  Total de aulas alocadas: {len(self._alocacoes)}\n")

    def listar_professores(self) -> None:
        if not self._professores:
            print("\n[AVISO] Nenhum professor cadastrado.")
            return
        print("\n--- Professores cadastrados ---")
        for prof in self._professores:
            print(f"  {prof}")          

    def listar_turmas(self) -> None:
        if not self._turmas:
            print("\n[AVISO] Nenhuma turma cadastrada.")
            return
        print("\n--- Turmas cadastradas ---")
        for turma in self._turmas:
            print(f"  {turma}")          
