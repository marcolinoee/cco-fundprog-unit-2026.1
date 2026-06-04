nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  ", "  maria"]
notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
consulta = "carla silva"

# Etapa 1: padronizar nomes
nomes_padronizados = []
for nome in nomes_brutos:
    nomes_padronizados.append(nome.strip().title())

# Etapa 2: filtrar notas aprovadas (>= 7.0)
aprovados = []
for nota in notas:
    if nota >= 7.0:
        aprovados.append(nota)

# Etapa 3: verificar presença do nome consultado
consulta_padronizada = consulta.strip().title()
encontrado = False
for nome in nomes_padronizados:
    if nome == consulta_padronizada:
        encontrado = True
        break

# Etapa 4: relatório final
print("=" * 40)
print("        RELATÓRIO FINAL")
print("=" * 40)

print("\nNomes padronizados:")
for nome in nomes_padronizados:
    print(f"  - {nome}")

print(f"\nNotas aprovadas (>= 7.0): {aprovados}")
print(f"Total de aprovados: {len(aprovados)}")

print(f"\nConsulta de presença: '{consulta_padronizada}'")
if encontrado:
    print(f"  -> {consulta_padronizada} está presente.")
else:
    print(f"  -> {consulta_padronizada} não está presente.")

print("=" * 40)
