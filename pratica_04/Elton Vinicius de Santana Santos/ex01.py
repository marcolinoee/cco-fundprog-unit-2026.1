nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]

def formatar_nomes(nomes):
    nomes_padronizados = []
    
    for nome in nomes:
        
        nome_padronizado = nome.strip().title()
        # strip() remove os espaços em branco no início e no final do nome
        # title() coloca a primeira letra de cada palavra em maiúscula e as demais em minúscula
        nomes_padronizados.append(nome_padronizado)
        # append() adiciona o nome padronizado à lista de nomes padronizados

    return f"Lista de nomes formatados: {', '.join(nomes_padronizados)} o total de nomes formatados é {len(nomes_padronizados)}"

nomes_formatados = formatar_nomes(nomes_brutos)
print(nomes_formatados)

'''
join() é um método de string que junta os elementos de uma lista em uma única string, 
usando um separador especificado. No exemplo acima, o separador é ", ", o que significa 
que os nomes formatados serão separados por vírgula e espaço na string final.

len() é uma função embutida do Python que retorna o número de itens em um objeto. 

'''