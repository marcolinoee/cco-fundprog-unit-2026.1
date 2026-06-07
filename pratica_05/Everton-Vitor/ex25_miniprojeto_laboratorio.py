# Modelagem inicial: 4 fileiras (linhas) e 5 computadores por fileira (colunas)
laboratorio = [
    ["L", "O", "L", "M", "L"],
    ["O", "O", "L", "L", "L"],
    ["L", "M", "O", "O", "L"],
    ["L", "L", "L", "M", "O"]
]

while True:
    # 1. Exibir o mapa completo de forma legível
    print("\n========= MAPA ATUAL DO LABORATÓRIO =========")
    print("      C0  C1  C2  C3  C4")
    for idx, fileira in enumerate(laboratorio):
        print(f"F{idx} | " + "   ".join(fileira) + " |")
    print("=============================================")
    
    # 2. Contar computadores por categoria de estado
    livres = 0
    ocupados = 0
    manutencao = 0
    for fileira in laboratorio:
        for pc in fileira:
            if pc == "L": libres += 1
            elif pc == "O": ocupados += 1
            elif pc == "M": manutencao += 1
            
    print(f"Estatísticas: [{livres}] Livres | [{ocupados}] Ocupados | [{manutencao}] Em Manutenção")
    
    print("\nMenu: Escolha uma fileira e computador para alocar ou digite -1 para sair.")
    f_usuario = int(input("Digite a fileira desejada (0-3): "))
    if f_usuario == -1:
        print("Encerrando o gerenciamento do laboratório.")
        break
        
    c_usuario = int(input("Digite o computador desejado (0-4): "))
    
    # 5. Informar se a posição digitada está fora dos limites
    if 0 <= f_usuario < 4 and 0 <= c_usuario < 5:
        estado_atual = laboratorio[f_usuario][c_usuario]
        
        # 3. Permitir ocupar uma posição livre informada pelo usuário
        if estado_atual == "L":
            laboratorio[f_usuario][c_usuario] = "O"
            print("Sucesso: Computador alocado com êxito!")
        # 4. Impedir ocupar uma posição em manutenção ou já ocupada
        elif estado_atual == "M":
            print("Bloqueado: Este computador está em manutenção. Escolha outro.")
        else:
            print("Aviso: Este computador já está ocupado por outro usuário.")
    else:
        print("Erro crítico: Posição inválida! Digite coordenadas válidas (Fileiras 0-3 e Computadores 0-4).")

# O que representa cada linha e cada coluna?
# Cada linha representa uma fileira física de mesas ordenadas dentro da infraestrutura do laboratório.
# Cada coluna representa a máquina/computador individual alocado horizontalmente naquela respectiva mesa.