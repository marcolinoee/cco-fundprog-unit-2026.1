maior = 0

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    
    if maior is 0 or nota > maior:
        maior = nota

print("A maior nota é:", maior)