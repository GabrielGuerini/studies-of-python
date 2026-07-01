# Lista de tarefas iniciais
tarefas = [
    {
        'tarefa': 'Acordar 9 Horas',
        'feita': True
    }
]

# Listar tarefas
def listar_tarefas():

    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada!')
        return

    print('=' * 30, 'LISTA TAREFAS', '=' * 30)

    for indice, tarefa in enumerate(tarefas, start=1):

        status = 'Feita' if tarefa['feita'] else 'Falhei'

        print(f'''
{indice} - {tarefa['tarefa']}
Status: {status}
''')


# Adicionar tarefa
def adicionar_tarefa():

    nome = input('Adicionar tarefa: ')

    nova_tarefa = {
        'tarefa': nome,
        'feita': False
    }

    tarefas.append(nova_tarefa)

    print('Tarefa adicionada!')

#Remover tarefa
def remover_tarefa():

    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada!')
        return

    listar_tarefas()

    indice = int(input('Digite a tarefa que deseja remover: '))

    if indice < 1 or indice > len(tarefas):
        print('Opção inválida!')
        return

    # remover tarefa aqui

    print('Tarefa removida!')


# Marcar tarefa como concluída
def marcar_status_tarefa():

    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada!')
        return

    listar_tarefas()

    indice = int(input('Qual tarefa deseja concluir? '))

    if indice < 1 or indice > len(tarefas):
        print('Tarefa inválida!')
        return

    tarefas[indice - 1]['feita'] = True

    print('Tarefa concluída!')


# Menu
def menu():

    print('''
==== MENU ====

1 - ADICIONAR TAREFA
2 - REMOVER TAREFA
3 - LISTAR TAREFAS
4 - MARCAR STATUS TAREFA
5 - SAIR
''')


# Main
print('=' * 30, 'LISTA DE TAREFAS DIÁRIAS', '=' * 30)

while True:

    menu()

    opcao = input('Digite sua escolha: ')

    if opcao == '1':
        adicionar_tarefa()

    elif opcao == '2':
        remover_tarefa()

    elif opcao == '3':
        listar_tarefas()
    
    elif opcao == '4':
        marcar_status_tarefa()

    elif opcao == '5':
        print('ENCERRANDO PROGRAMA!')
        break

    else:
        print('OPÇÃO INCORRETA, DIGITE NOVAMENTE!')