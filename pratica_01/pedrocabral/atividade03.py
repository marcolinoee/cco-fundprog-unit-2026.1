fatias = int(input("quantas fatias de pizza tem no total? "))
devs = int(input("quantos devs vão comer? "))
fatias_por_dev = fatias // devs
print(f"cada dev pode comer {fatias_por_dev} fatias de pizza")
sobras = fatias % devs
print(f"sobram {sobras} fatias de pizza")