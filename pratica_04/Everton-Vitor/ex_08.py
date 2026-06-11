# Dados sugeridos
itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]

# Inicialização dos contadores
qtd_mouse = 0
qtd_teclado = 0
qtd_monitor = 0  # Para o desafio opcional

# Tarefas 1, 2 e Desafio: Percorrendo e contando
for item in itens:
    if item == "mouse":
        qtd_mouse += 1
    elif item == "teclado":
        qtd_teclado += 1
    elif item == "monitor":
        qtd_monitor += 1

# Tarefa 3: Exibindo com frases completas
print(f"O item 'mouse' aparece {qtd_mouse} vezes na lista.")
print(f"O item 'teclado' aparece {qtd_teclado} vezes na lista.")
print(f"O item 'monitor' (desafio) aparece {qtd_monitor} vez(es) na lista.")