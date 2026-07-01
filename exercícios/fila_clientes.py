clientes = []


def adicionar_cliente():
    cliente = input('Nome do cliente: ')
    clientes.append(cliente)


def nenhum_cliente():
    if not clientes:
        print('Nenhum cliente para atender')
        return True
    return False


def atender_proximo_cliente():
    if nenhum_cliente():
        return

    print(f'O proximo cliente é: {clientes[1]}')


def mostrar_fila():
    for i, cliente in enumerate(clientes, start=1):
        print(f'''
Fila de clientes: 
{clientes}''')


def remover_cliente():
    clientes.pop(0)


def atender_cliente():
    if nenhum_cliente():
        return
    print(f'O primeiro atendimento será do cliente:{clientes[0]}')
    print(f'O cliente{clientes[0]} foi atendido.')
    remover_cliente()


def atendimento_cliente():
    while True:
        if nenhum_cliente():
            return
        pergunta = input('O cliente foi atendido? S/N: ')

        if pergunta.lower() == 's':
            print(f'O primeiro atendimento será do cliente:{clientes[0]}')
            print(f'O cliente{clientes[0]} foi atendido.')
            remover_cliente()
            atender_proximo_cliente()
        elif pergunta.lower():
            print('Aguardando o atendimento...')
        else:
            print('Opção inválida')
