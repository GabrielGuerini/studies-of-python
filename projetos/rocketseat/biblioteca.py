# ==========================
# Biblioteca Canoense
# ==========================

# Lista inicial de livros
livros = [
    {
        'titulo': 'Harry Potter',
        'autor': 'J.K. Rowling',
        'disponivel': True
    },
    {
        'titulo': 'Maze Runner',
        'autor': 'James Dashner',
        'disponivel': False
    },
    {
        'titulo': 'Crime e Castigo',
        'autor': 'Fiódor Dostoiévski',
        'disponivel': False
    },
    {
        'titulo': 'Paraíso',
        'autor': 'Dante',
        'disponivel': True
    },
    {
        'titulo': 'A Hora da Estrela',
        'autor': 'Clarice Lispector',
        'disponivel': True
    }
]


# ==========================
# FUNÇÃO PARA LISTAR LIVROS
# ==========================
def listar_livros():

    print('\n===== LIVROS DA BIBLIOTECA =====')

    # percorre todos os livros da lista
    for indice, livro in enumerate(livros, start=1):

        # transforma True/False em texto
        status = 'Disponível' if livro['disponivel'] else 'Indisponível'

        print(f'''
{indice}. {livro['titulo']}
Autor: {livro['autor']}
Status: {status}
''')


# ==========================
# FUNÇÃO PARA CADASTRAR LIVRO
# ==========================
def cadastrar_livro():

    print('\n===== CADASTRAR LIVRO =====')

    titulo = input('Digite o título do livro: ')
    autor = input('Digite o autor do livro: ')

    # cria um novo dicionário
    novo_livro = {
        'titulo': titulo,
        'autor': autor,
        'disponivel': True
    }

    # adiciona o livro na lista
    livros.append(novo_livro)

    print('\nLivro cadastrado com sucesso!')


# ==========================
# FUNÇÃO PARA LOCAR LIVRO
# ==========================
def locar_livro():

    print('\n===== LOCAÇÃO DE LIVRO =====')

    # mostra os livros primeiro
    listar_livros()

    try:

        numero = int(input('\nDigite o número do livro: '))

        # converte para posição da lista
        livro = livros[numero - 1]

        if livro['disponivel']:

            livro['disponivel'] = False

            print(f"\nVocê locou '{livro['titulo']}' com sucesso!")

        else:

            print('\nEsse livro já está locado.')

    except:

        print('\nLivro inválido.')


# ==========================
# MENU PRINCIPAL
# ==========================
def menu():

    print('''
===== MENU =====

1 - Ver livros
2 - Locar livro
3 - Cadastrar livro
4 - Sair
''')


# ==========================
# PROGRAMA PRINCIPAL (MAIN)
# ==========================

print('=' * 30, 'Biblioteca Canoense', '=' * 30)

nome = input('Bem-vindo! Digite seu nome: ')

print(f'\nOlá, {nome}!')

while True:

    menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':

        listar_livros()

    elif opcao == '2':

        locar_livro()

    elif opcao == '3':

        cadastrar_livro()

    elif opcao == '4':

        print('\nObrigado por utilizar a Biblioteca Canoense!')
        break

    else:

        print('\nOpção inválida.')