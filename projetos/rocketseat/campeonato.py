# lista inicial de time:
times = [
    {
        'nome': 'Paysandu',
        'pontos': 8
    }
]

# =====================================================================#
# função cadastrar times:


def cadastrar_time():
    nome = input('Digite o nome do time: ')
    pontos = int(input('Digite a quantidades de pontos que o time fez: '))

    # Dicionário novo
    novo_time = {
        'nome': nome,
        'pontos': pontos
    }

    # adicionando o novo time e sua pontuação.
    times.append(novo_time)

    print('O time e sua pontuação foram cadastrados no sistema!')

# =================================================================#

# Ordenar times pela pontuação.


def ordenar_times():
    times_ordenados = sorted(
        times,
        key=lambda time: time['pontos'],
        reverse=True
    )
    return times_ordenados


# função mostrar tabela:
def mostrar_tabela():

    # nenhum time inscrito retorna.
    if len(times) == 0:
        print('Nenhum time foi inscrito no campeonato!')
        return

    # chamando a função ordenar, para mostrar a ordem da tabela pelos pontos.
    times_ordenados = ordenar_times()

    # reutilização dos times ordenados para aparecer no print.
    for i, time in enumerate(times_ordenados):
        print(
            f'{i + 1} - {time["nome"]} | '
            f'{time["pontos"]} pontos'
        )

# ===================================================#


def buscar_time():
    buscar = input('Digite o nome do time: ')

    # Caso não tenha nenhum time inscrito.
    if len(times) == 0:
        print('Nenhum time foi inscrito.')
        return

    # buscando time:
    for time in times:

        if time['nome'].lower() == buscar.lower():

            print('Time encontrado!')

            print(f"Nome: {time['nome']}")
            print(f"Pontos: {time['pontos']}")
            return

    print('Esse time não foi inscrito.')

# mostrar líder do campeonato.


def mostrar_lider():

    # nenhum time inscrito
    if len(times) == 0:
        print('Nenhum time foi inscrito.')
        return

    # chamando a ordem de pontuação.
    times_ordenados = ordenar_times()
    lider = times_ordenados[0]

    print(
        f'O Líder do campeonato é {lider["nome"]} com {lider["pontos"]} pontos')


# alterando a pontuação de um time:
def alterar_pontuacao():

    # nenhum time
    if len(times) == 0:
        print('Nenhum time foi inscrito.')
        return

    nome = input('Digite o nome do time que você quer alterar a pontuação: ')

    # alterando a pontuação
    for time in times:

        if time['nome'].lower() == nome.lower():

            nova_pontuacao = int(input('Digite a nova pontuação: '))

            time['pontos'] = nova_pontuacao

            print('Pontuação alterada com sucesso!')
            return

    print('Esse time não foi inscrito.')


# MENU
# MENU
def menu():

    while True:

        print('''
===== MENU =====

1 - Cadastrar time
2 - Mostrar tabela
3 - Mostrar líder
4 - Alterar pontuação
5 - Buscar time
6 - Sair
''')

        opcao = int(input('Digite sua escolha: '))

        if opcao == 1:
            cadastrar_time()

        elif opcao == 2:
            mostrar_tabela()

        elif opcao == 3:
            mostrar_lider()

        elif opcao == 4:
            alterar_pontuacao()

        elif opcao == 5:
            buscar_time()

        elif opcao == 6:
            print('Encerrando o programa!')
            break

        else:
            print('Opção inválida, tente novamente.')


# main
menu()
