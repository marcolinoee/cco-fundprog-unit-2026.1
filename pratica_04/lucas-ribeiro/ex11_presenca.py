presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
presentes_padronizado = [nome.strip().title() for nome in presentes_bruto]
consulta = "João"
situacao = False
for nome in presentes_padronizado:
    if nome == consulta:
        situacao = True
    else:
         continue

        
print(f'Alunos presentes: {presentes_padronizado}\nAluno: {consulta}\nO aluno esá presente?: {situacao}')