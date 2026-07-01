# Sistema ctrl + z, usando pilhas.

mensagens = []


def adiocionar_msg():
    m = input('Digite sua mensagem: ')
    mensagens.append(m)


def desfazer_msg():
    if nenhuma_msg():
        return
    mensagem = mensagens.pop()
    print(f'Mensagem desfeita: {mensagem}')


def nenhuma_msg():
    if not mensagens == 0:
        print('Nenhuma mensagem recente para remover')
        return True
    return False


def historico():
    if nenhuma_msg():
        return
    for i, mensagem in enumerate(mensagens, start=1):
        print(i, mensagem)


def ultima_msg():
    if nenhuma_msg():
        return
    print(mensagens[-1])


def menu():
    while True:
        print('''
    1 - escrever mensagem
    2 - desfazer mensagem
    3 - histórico
    4 - ultíma mensagem
    5 - sair
          ''')
        opcao = int(input('Digite sua opção: '))

        if opcao == 1:
            adiocionar_msg()
        elif opcao == 2:
            desfazer_msg()
        elif opcao == 3:
            historico()
        elif opcao == 4:
            ultima_msg()
        elif opcao == 5:
            break
        else:
            print('Opção invalida.')
