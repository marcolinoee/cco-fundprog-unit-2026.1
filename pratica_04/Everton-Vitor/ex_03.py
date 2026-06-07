palavra = "algoritmo"
notas = [7.0, 8.5, 6.0, 9.0, 7.5]

print(f"Primeira letra da palavra: {palavra[0]}")
'''
em python o primeiro elemento de uma string ou lista é acessado com o índice 0,
então palavra[0] retorna a primeira letra da string "algoritmo", que é "a". 
Por que o índice começa em 0? 
Isso é uma convenção em muitas linguagens de programação, incluindo Python, 
e tem raízes históricas na forma como a memória é endereçada em computadores. 
'''


print(f"Última letra da palavra: {palavra[3]}")
print(f"Primeira nota: {notas[0]}")
print(f"Última nota: {notas[-1]}")