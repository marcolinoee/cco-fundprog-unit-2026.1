sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

L = 0
O = 0

for i in range(len(sala)):
    for j in range(len(sala[0])):
        if sala[i][j] == "L":
            L += 1
        else:
            O += 1
            
print(f"Lugares livres: {L}")
print(f"Lugares ocupados: {O}")
