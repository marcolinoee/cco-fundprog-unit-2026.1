# main.py

from entidades_poo import Aluno, Professor, Disciplina, Turma
from motor_alocacao import MotorAlocacao
from matriz_diario  import lancar_notas, gerar_relatorio_ascii, processar_diario, adicionar_aluno
from menus_interface import Menu

def main():
    motor  = MotorAlocacao()
    menu   = Menu()
    alunos = []

    while True:
        opcao = menu.exibir_principal()

        if opcao == "0":
            print("Sistema encerrado.")
            break

        elif opcao == "1":               
            nome, carga = menu.coletar_dados_professor()
            prof = Professor(nome, carga)
            motor.cadastrar_professor(prof)
            print(f"=== {prof} cadastrado! ===")

        elif opcao == "2":               
            nome, matricula = menu.coletar_dados_aluno()
            aluno = Aluno(nome, matricula)
            adicionar_aluno(alunos, aluno)
            print(f"=== {aluno} cadastrado! ===")
        
        elif opcao == "3":               
            menu.fluxo_alocacao(motor)

        elif opcao == "4":               
            diario = lancar_notas()
            resultado =processar_diario(diario)

        elif opcao == "5":               
            gerar_relatorio_ascii(resultado)

main()