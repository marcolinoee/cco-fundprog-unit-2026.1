class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    def __repr__(self):
        return f"Aluno({self.nome!r}, mat={self.matricula!r})" 
    

class Disciplina:
    def __init__(self, nome: str, codigo: str):
        self.nome = nome
        self.codigo = codigo

    def __repr__(self):
        return f"Disciplina({self.nome!r}, cod={self.codigo!r})"
    
class Professor:
    def __init__(self, nome: str, carga_max: int = 20):
        self.nome = nome
        self.carga_max = carga_max
        self.aulas = [] 
    

    def adicionar_aula(self, slot: str) -> bool:
        if len(self.aulas) >= self.carga_max:
            print(
                f"[BLOQUEADO] Prof. {self.nome} já atingiu o limite "
                f"de {self.carga_max} aula(s). Slot '{slot}' recusado."
            )
            return False

        self.aulas.append(slot)
        print(
            f"[OK] Slot '{slot}' adicionado para Prof. {self.nome}. "
            f"({len(self.aulas)}/{self.carga_max} slots ocupados)"
        )
        return True

    def carga_atual(self) -> int:
        return len(self.aulas)

    def __repr__(self):
        return (
            f"Professor({self.nome!r}, "
            f"carga={self.carga_atual()}/{self.carga_max})"
        )

class Turma:
    def __init__(self, codigo: str, professor: Professor, disciplina: Disciplina):
        self.codigo = codigo
        self.professor = professor
        self.disciplina = disciplina
        self.alunos: list[Aluno] = []

    def adicionar_aluno(self, aluno: Aluno) -> None:
        self.alunos.append(aluno)
        print(f"[OK] {aluno.nome} adicionado(a) à turma {self.codigo}.")

    def listar_alunos(self) -> None:
        print(f"\n=== Turma {self.codigo} | {self.disciplina.nome} "f"| Prof. {self.professor.nome} ===")
        if not self.alunos:
            print("  (nenhum aluno matriculado)")
        else:
            for i, aluno in enumerate(self.alunos, start=1):
                print(f"  {i:02d}. {aluno.nome}  [{aluno.matricula}]")
        print(f"  Total: {len(self.alunos)} aluno(s)\n")

    def __repr__(self):
        return (
            f"Turma({self.codigo!r}, "
            f"prof={self.professor.nome!r}, "
            f"disc={self.disciplina.nome!r}, "
            f"alunos={len(self.alunos)})"
        )