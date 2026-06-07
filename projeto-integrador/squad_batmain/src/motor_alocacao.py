def exibir_slots():
    print(f'''
        {'='*5} Aulas/Turnos {'='*5}

        Selecione um slot para alocação:

        [1] Segunda Manhã
        [2] Segunda Noite
        [3] Terça Manhã
        [4] Terça Noite
        [5] Quarta Manhã
        [6] Quarta Noite
        [7] Quinta Manhã
        [8] Quinta Noite
        [9] Sexta Manhã
        [10] Sexta Noite
  ''')
def verificar_slots():
    while True: 
        try:
            exibir_slots()
            slot = int(input('      ==> ').strip())
            if slot < 1 or slot > 10:
                print('Valor inválido! Digite um número de 1 a 10...')
                continue
            return slot
        except ValueError:
            print('Valor inválido! Digite novamente...')
            continue
def dias_slots(opcao):
    if opcao == 1:
        return 'Segunda/Manhã'
    elif opcao == 2:
        return 'Segunda/Noite'
    elif opcao == 3:
        return 'Terça/Manhã'
    elif opcao == 4:
        return 'Terça/Noite'
    elif opcao == 5:
        return 'Quarta/Manhã'
    elif opcao == 6:
        return 'Quarta/Noite'
    elif opcao == 7:
        return 'Quinta/Manhã'
    elif opcao == 8:
        return 'Quinta/Noite'
    elif opcao == 9:
        return 'Sexta/Manhã'
    elif opcao == 10:
        return 'Sexta/Noite'
    return 'Vazio'


      
    

def verificar_choque_slots(slot_novo, professor_novo, turma_novo, slot_a1, professor_a1, turma_a1, slot_a2,  professor_a2, turma_a2):
    choque_prof_a1 = (professor_novo == professor_a1) and (slot_novo == slot_a1)
    choque_prof_a2 = (professor_novo == professor_a2) and (slot_novo == slot_a2)
    choque_turma_a1 = (turma_novo == turma_a1) and (slot_novo == slot_a1)
    choque_turma_a2 = (turma_novo == turma_a2) and (slot_novo == slot_a2)
    if choque_prof_a1 or choque_prof_a2 or choque_turma_a1 or choque_turma_a2:
        return True
    return False

def slots_cadastrados(slot):
    print(f'''
    {'='*21} Aulas já alocadas {'='*21}
        {'Nenhum slot cadastrado' if not slot else slot}
    {'='*61}
            ''')

def cadastrar_aula():
    professor_a1 = 'Prof. Jorge'
    turma_a1 = 'Direito'
    slot_a1 = 2
    professor_a2 = 'Prof. Roberto'
    turma_a2 = 'Téc. Enfermagem'
    slot_a2 = 3
    exibir = f'\n Slot({slot_a1}): \n\n {professor_a1} \n {turma_a1} \n {dias_slots(slot_a1)} \n\n Slot({slot_a2}): \n\n {professor_a2} \n {turma_a2} \n {dias_slots(slot_a2)}\n\n'
    while True:
        
        slots_cadastrados(exibir)


        professor_novo = str(input('Informe qual professor você deseja cadastrar: ').title().strip())
        
        turma_novo = str(input('Disciplina que deseja alocar: ').title().strip())
        
        slot_novo = verificar_slots()
    
    
    
        choque = verificar_choque_slots(slot_novo, professor_novo, turma_novo, slot_a1, professor_a1, turma_a1, slot_a2,  professor_a2, turma_a2)
        if choque == True:
            print('Choque de aulas! Informe os dados novamente...')
            continue
        else:
            print('Aulas cadastradas com sucesso!')
            exibir += f'Slot({slot_novo}): \n\n Prof. {professor_novo} \n {turma_novo} \n {dias_slots(slot_novo)}\n\n'
            slots_cadastrados(exibir)
            break


