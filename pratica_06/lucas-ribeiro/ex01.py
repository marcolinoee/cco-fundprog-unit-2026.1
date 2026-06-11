class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    def __repr__(self):
        return f'Aluno: {self.nome!r}\nMatrícula: {self.matricula!r}'

print(Estudante('Lucas', 1276489))