usuario = str(input("qual o seu nome? "))
nascimento = int(input("qual o ano que voce nasceu? "))
ano_atual = 2026
idade_atual = ano_atual - nascimento
altura_cm = float(input("qual a sua altura? "))
altura = altura_cm / 100
print(f"seu nome é {usuario}, voce tem {idade_atual} anos e sua altura é {altura:.2f} metros")
