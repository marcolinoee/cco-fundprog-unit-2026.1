maior_nota = 0
for i in range(1, 6):
    nota = float(input(f"digite a {i}ª nota: "))
    if nota > maior_nota:
        maior_nota = nota
print(f"A maior nota é: {maior_nota}")

        
