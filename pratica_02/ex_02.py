pessoas = {
    'João': 25,
    'Maria': 30,
    'Pedro': 12,
    'Ana': 63
}

def lerIdade(pessoas):
    for nome, idade in pessoas.items():

        if idade >= 18 and idade < 60:
            print(f"{nome} tem {idade} anos e é maior de idade.")

        elif idade < 18:
            print(f"{nome} tem {idade} anos e é menor de idade.")
        
        else:
            print(f"{nome} tem {idade} anos e é idoso/a.")

lerIdade(pessoas)
        