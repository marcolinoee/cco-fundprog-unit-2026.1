itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]

def contar_mouse_e_teclado(lista):
    return f"Mouse: {lista.count('mouse')}, Teclado: {lista.count('teclado')}"

print(contar_mouse_e_teclado(itens))