
perguntas = [
    "O número total de fatias?",
    "O número de programadores na equipe?"
]
    
respostas = []
    
for pergunta in perguntas:
    resposta = int(input(pergunta + " "))
    respostas.append(resposta)

def calcular_fatias_por_programador(total_fatias, total_programadores):
    if total_programadores == 0:
        return "Não é possível dividir por zero."
    fatias_por_programador = total_fatias / total_programadores
    return f"Cada programador receberá {fatias_por_programador:.2f} fatias de pizza."

def sobra(total_fatias, total_programadores):
    if total_programadores == 0:
        return "Não é possível dividir por zero."
    fatias_sobrando = total_fatias - total_programadores
    return f"Restarão {fatias_sobrando} fatias de pizza."

print("Fatias por programador:", calcular_fatias_por_programador(respostas[0], respostas[1]))
print("Fatias sobrando:", sobra(respostas[0], respostas[1]))






    
