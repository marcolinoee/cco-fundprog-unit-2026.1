total_fatias = int(input("Digite o número total de fatias: "))
programadores = int(input("Digite o número de programadores na equipe: "))

fatias_por_pessoa = total_fatias // programadores
sobra = total_fatias % programadores

print("=== DIVISÃO DA PIZZA ===")
print("Fatias por pessoa: {}".format(fatias_por_pessoa))
print("Sobra na caixa:    {}".format(sobra))