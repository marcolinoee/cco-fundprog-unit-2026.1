# --- ETAPA 1: Dados Brutos do Sistema ---
estudantes_bruto = ["  gabriel ", "ALINE", "  bBeatriz ", "caio ", "Aline"]
notas_bruto = [8.5, 5.0, 7.5, 4.0, 9.0]
nome_pesquisa = "  aline  "

# --- ETAPA 2: Padronização e Filtragem (Operações com Strings e Listas) ---
estudantes_limpos = []
for nome in estudantes_bruto:
    estudantes_limpos.append(nome.strip().capitalize()) # Remove espaços e padroniza Inicial Maiúscula

notas_aprovadas = []
for nota in notas_bruto:
    if nota >= 7.0:
        notas_aprovadas.append(nota)

pesquisa_limpa = nome_pesquisa.strip().capitalize()

# --- ETAPA 3: Busca Simples (Verificação de Presença) ---
esta_presente = pesquisa_limpa in estudantes_limpos

# --- ETAPA 4: Exibição do Relatório Final ---
print("=========================================")
print("       RELATÓRIO FINAL DA TURMA          ")
print("=========================================")
print(f"Estudantes Cadastrados: {estudantes_limpos}")
print(f"Notas dos Aprovados (>= 7.0): {notas_aprovadas}")
print(f"Total de alunos aprovados: {len(notas_aprovadas)}")
print("-----------------------------------------")
print(f"Busca por estudante: '{pesquisa_limpa}'")
if esta_presente:
    print("Resultado da Busca: Estudante PRESENTE na listagem.")
else:
    print("Resultado da Busca: Estudante AUSENTE na listagem.")
print("=========================================")