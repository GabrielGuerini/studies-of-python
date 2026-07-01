
livros = []


def inserir_livro():
    x = input('Digite o nome do livro: ')
    livros.append(x)


def remove_livro():
    if nenhum_livro():
        return
    livros.pop()


def mostrar_livro():
    if nenhum_livro():
        return
    print(livros)


def nenhum_livro():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return True
    return False


def menu():

    print('''
1 - inserir livro
2 - remover o ultimo livro
3 - mostrar livros
4 - sair        
          ''')


while True:
    menu()
    opcao = int(input('Digite sua opoção: '))

    if opcao == 1:
        inserir_livro()
    elif opcao == 2:
        remove_livro()
    elif opcao == 3:
        mostrar_livro()
    elif opcao == 4:
        break
    else:
        print('Opção não encontrada')
