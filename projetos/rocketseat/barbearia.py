from heapq import heappush, heappop

clientes = []


def menu():
    print('''
    1 - cadastrar clientes
    2 - Ver clientes
    3 - Sair
          ''')
    while True:

        opcao = int(input('Digite sua opção: '))

        if opcao == 1:
            cadastrar_clientes()
        elif opcao == 2:
            mostrar_clientes()
        elif opcao == 4:
            break
        print('Opcão errada.')


def voltar_menu():
    input('Aperte Enter para voltar ao menu...')
    return


def cadastrar_clientes():

    nome = input('Nome do cliente: ')
    servico = input('Digite o nome do serviço: ')
    assinante = input('O cliente é assinante? S/N: ')

    if assinante.lower() == 's':
        prioridade = 1
    else:
        prioridade = 2

    heappush(clientes, (prioridade, nome, servico))

    print('Cliente cadastrado com sucesso!')
    voltar_menu()


def mostrar_clientes():

    if not clientes:
        print('Nenhum cliente')
        voltar_menu()
        return

    print('Fila de atendimento em ordem prioritária.')

    while clientes:
        prioridade, nome, servico = heappop(clientes)
        print(f'{nome}, {prioridade}, {servico}')


menu()
