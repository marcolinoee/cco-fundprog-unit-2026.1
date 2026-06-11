ex_12.py
# Dados sugeridos
presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

# Tarefa 1: Criando a lista padronizada
presentes_limpo = []
for nome in presentes_bruto:
    # strip() remove espaços nas pontas e lower() deixa tudo em minúsculo
    presentes_limpo.append(nome.strip().lower())

# Tarefa 2: Padronizando a consulta
consulta_limpa = consulta.strip().lower()

# Tarefa 3 e 4: Verificação e exibição
print("Lista padronizada:", presentes_limpo)

if consulta_limpa in presentes_limpo:
    print(f"O estudante '{consulta}' está PRESENTE.")
else:
    print(f"O estudante '{consulta}' está AUSENTE.")
    
# Desafio opcional: Para testar um nome ausente, basta mudar a variável consulta para "Carlos"