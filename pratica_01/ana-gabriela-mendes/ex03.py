TotalFatias = int(input("Digite o número total de fatias: "))
TotalPessoas = int(input("Digite o número total de programadores: "))
FatiasPorPessoa = TotalFatias // TotalPessoas
sobras = TotalFatias % TotalPessoas
print(f"Cada programador receberá {FatiasPorPessoa} fatias de pizza e sobrará {sobras} fatias.")

