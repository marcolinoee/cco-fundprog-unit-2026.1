
tarefas_academicas = []

def adicionar_tarefa(tarefa):
    tarefas_academicas.append(tarefa)
    return f"Tarefa '{tarefa}' adicionada com sucesso!"

def listar_tarefas():
    if not tarefas_academicas:
        return "Nenhuma tarefa acadêmica cadastrada."
    return "Tarefas Acadêmicas:\n" + "\n".join(f"- {tarefa}" for tarefa in tarefas_academicas)

while True:
    contador = len(tarefas_academicas)
    print(f"\nVocê tem {contador} tarefa(s) acadêmica(s) cadastrada(s).")
    tarefa = input("Digite a tarefa acadêmica que deseja adicionar ou 'sair' para encerrar: ")

    if tarefa.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break

    adicionar_tarefa(tarefa)
    print(listar_tarefas())



