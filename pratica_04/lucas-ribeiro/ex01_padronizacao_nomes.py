nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]

nomes_padronizados = [nome.strip().title() for nome in nomes_brutos]

print(f'Lista de nomes brutos: {nomes_brutos}\nLista de nomes padronizados: {nomes_padronizados}')