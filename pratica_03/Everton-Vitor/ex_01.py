import time

def Saudacao(name):
    return f"Bem-vindo(a), {name}!"

list_names = ["Alice", "Bob", "Charlie"]

for name in list_names:
    print(Saudacao(name))
    time.sleep(1)