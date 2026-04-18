nomeUsuario = str (input("Qual o seu nome? "))
anoNascimento = int (input("Qual o ano do seu nascimento? Digite apenas números. "))
altura = float (input("Qual a sua altura? (Ex: 1.76) "))
idade = 2026 - anoNascimento

print(f"Olá, {nomeUsuario}! Você tem {idade} anos e sua altura é de {altura}m. Seja bem-vindo(a)")