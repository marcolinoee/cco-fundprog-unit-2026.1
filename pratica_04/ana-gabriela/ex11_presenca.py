presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

presentes = []
for nome in presentes_bruto:
    presentes.append(nome.strip().title())

consulta_padronizada = consulta.strip().title()

encontrado = False
for nome in presentes:
    if nome == consulta_padronizada:
        encontrado = True
        break

print(f"Lista de presentes: {presentes}")

if encontrado:
    print(f"{consulta_padronizada} está presente.")
else:
    print(f"{consulta_padronizada} não está presente.")
