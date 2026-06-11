def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

# Exemplo de uso da função Normal
print(calcular_total(50, 2))
print(calcular_total(100, 5))
print("")
# Exemplo de uso da função limitrofe
print(calcular_total(50, 1))
print("")
# Exemplo de uso da função extremo
print(calcular_total(0, 29))

