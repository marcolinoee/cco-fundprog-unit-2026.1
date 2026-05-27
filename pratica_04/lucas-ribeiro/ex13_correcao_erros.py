
# 
lista = [3, 1, 2]
resultado = lista.sort()
# print(resultado) --> Implicara em None pois o . sort() ordena diretamente a lista original, não restornado uma nova lista
print(lista) # --> Maneira correta


nomes = ["Ana", "Bruno"]
# print(nomes[5]) --> Ocorre erro pelo fato da posição 5 não existir
# Casos corretos
print(nomes[0])
print(nomes[1])
