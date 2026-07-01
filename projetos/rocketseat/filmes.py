# Lista inicial de filme.
filmes = [{
    'genêro': 'Terror',
    'nome': 'O Exorcista',
    'nota': '10.0'
}
]

# Adicionar um filme:


def adicionar_filme():

    print('='*30, 'CADASTRO DE FILMES', '='*30)

    nome = input('Digite o nome do filme: ')
    nota = float(input('Dê uma nota de zero à dez pro filme: '))
    genero = input('Digite o genêro do filme: ')

    # Dicionário do novo filme
    novo_filme = {
        'genêro': genero,
        'nome': nome,
        'nota': nota
    }
    # adicionado a lista original.
    filmes.append(novo_filme)

    print('Filme adicionado com sucesso!')

# Função para mostrar um filme:


def mostrar_filmes():

    print('='*30, 'LISTA DE FILMES', '='*30)

    # caso não exista o filme solicitado:
    if len(filmes) == 0:
        print('Nenhum filme cadastrado.')
        return

    # print do filmes:
    for i, filme in enumerate(filmes):
        print(f"{i + 1} - {filme['nome']}")

# função Ranking filmes


def ranking_filmes():

    if len(filmes) == 0:
        print('Nenhum filme cadastrado.')
        return
# times ordenados pela nota uso da função lambda
    filmes_ordenados = sorted(
        filmes,
        key=lambda filme: filme['nota'],
        reverse=True
    )
    print('\n' + '=' * 30)
    print('RANKING DE FILMES')
    print('=' * 30)
    for i, filme in enumerate(filmes_ordenados):
        print(
            f'{i + 1} - {filme["nome"]} | '
            f'Nota: {filme["nota"]}'
        )

# função MENU:


def menu():

    while True:

        print('='*30, 'MENU', '='*30)
        print('''
        1 - Adicionar filme
        2 - Mostrar filmes
        3 - Mostrar melhores filmes
        4 - Sair
        ''')
        opcao = int(input('Digite a opão desejada: '))
        if opcao == 1:
            adicionar_filme()
        elif opcao == 2:
            mostrar_filmes()
        elif opcao == 3:
            ranking_filmes()
        elif opcao == 4:
            print('Encerrando o programa!')
            break
        else:
            print('Opção não encontrada!')


# main:
menu()
