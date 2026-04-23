print("="*50)
print("programa para dividir fatias de pizza entre uma equipe")
print("="*50)

Total_Fatias = int(input("O número total de fatias: "))
Programadores = int(input("O número de programadores na equipe: "))

Fatias_PorPessoa = Total_Fatias // Programadores
Sobra = Total_Fatias % Programadores

print("="*50)
print(f"Cada programador comerá: {Fatias_PorPessoa} fatias.")
print(f"Sobra na caixa: {Sobra} fatia(s).")
print("="*50)