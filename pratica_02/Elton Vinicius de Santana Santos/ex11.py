class Alunos:
    def __init__(self):
        self.aprovados = 0
        self.reprovados = 0
        self.recuperacao = 0

    def calcular_percentual(self):
        qtd = int(input("Digite a quantidade total de alunos: "))
        
        for i in range(qtd):
            media = float(input(f"Digite a média do aluno {i+1}: "))
            
            if media >= 7:
                self.aprovados += 1
            elif media >= 4:
                self.recuperacao += 1
            else:
                self.reprovados += 1

    def resultado(self):
        total = self.aprovados + self.reprovados + self.recuperacao
        
        print(f"Aprovados: {(self.aprovados / total) * 100:.2f}%")
        print(f"Recuperação: {(self.recuperacao / total) * 100:.2f}%")
        print(f"Reprovados: {(self.reprovados / total) * 100:.2f}%")


a = Alunos()
a.calcular_percentual()
a.resultado()