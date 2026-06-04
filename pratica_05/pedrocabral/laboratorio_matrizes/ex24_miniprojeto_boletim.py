boletim = [
    ["lebron", "durant", "curry", "irving", "kawhi"],
    [6.0, 7.5, 1.0, 8.5, 9.0],
    [8.0, 8.5, 2.5, 8.0, 6.5],
    [7.5, 8.0, 5.5, 7.0, 8.0],
    [8.5, 7.0, 2.0, 8.5, 9.5]
]

for i in range(len(boletim)):
    for j in range(len(boletim[0])):
        media = (boletim[1][j] + boletim[2][j] + boletim[3][j] + boletim[4][j]) / 4
        if media >= 7.0:
            print(f"aluno: {boletim[0][j]} média: {media} aprovado")
        elif media >= 5.0:
            print(f"aluno: {boletim[0][j]} média: {media} reprovado")
        else:
            print(f"aluno: {boletim[0][j]} média: {media} recuperaçao")
        
        