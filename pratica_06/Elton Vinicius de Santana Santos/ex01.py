class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print("Nota inválida")

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        return "Recuperação"


class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def preco_com_imposto(self):
        return self.preco + (self.preco * Produto.imposto_padrao)


class Turma:
    def __init__(self):
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def media_geral(self):
        soma = 0

        for estudante in self.estudantes:
            soma += estudante.calcular_media()

        return soma / len(self.estudantes)


e1 = Estudante("Ana", "001")
e1.adicionar_nota(8)
e1.adicionar_nota(7)
e1.adicionar_nota(9)

e2 = Estudante("Bruno", "002")
e2.adicionar_nota(5)
e2.adicionar_nota(6)
e2.adicionar_nota(5)

e3 = Estudante("Carla", "003")
e3.adicionar_nota(10)
e3.adicionar_nota(9)
e3.adicionar_nota(8)

turma = Turma()

turma.matricular(e1)
turma.matricular(e2)
turma.matricular(e3)

for estudante in turma.estudantes:
    print(
        estudante.nome,
        "- Média:",
        round(estudante.calcular_media(), 2),
        "-",
        estudante.situacao()
    )

print("Média geral da turma:", round(turma.media_geral(), 2))

produto = Produto("Mouse", 100)

print("Preço com imposto:", produto.preco_com_imposto())

print("Resposta 14: O erro ocorre quando usamos nome = nome em vez de self.nome = nome.")

print("Resposta 15: imposto_padrao é atributo de classe porque é compartilhado por todos os objetos da classe Produto.")

print("Resposta 15: nome, matricula, preco e notas são atributos de instância porque cada objeto possui seus próprios valores.")