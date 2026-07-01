# Lista inicial de Produtos.
produtos = []

# Cadastrar produtos:


def cadastrar_produtos():
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade de estoque do Produto: '))

    # Dicionário de Produtos:
    novo_produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }

    # Adicionando novo produto à lista:
    produtos.append(novo_produto)

    print('Produto adicionado ao estoque.')

# Ordenar produtos alfabeticámente:


def ordenar_produtos_nome():
    produtos_ordenados = sorted(
        produtos,
        key=lambda nome: nome['nome'],
        reverse=True
    )
    return produtos_ordenados

# Mostrar produtos:


def mostrar_produtos():
    # Caso não tenha produto:
    if len(produtos) == 0:
        print('Nenhum produto foi cadastrado no sistema.')
        return
    # chamando a funçao ordenada.
    produtos_ordenados = ordenar_produtos_nome()

    # Ordenando produtos
    for produto in produtos_ordenados:
        print(produto['nome'],
              '||',
              produto['preco'],
              '\n',
              '='*30,
              produto['quantidade'])

# Calcular Estoque de produto:


def calcular_estoque():

    # Variével ponto de partida
    valor_total = 0
    total_produtos = 0

    # calculos referentes aos produtos, quantidades(unidades), e valor em reais.
    for produto in produtos:
        total_produtos += produto['quantidade']
        valor_total += produto['preco'] * produto['quantidade']

        # Menu do estoque:
    print('='*30, 'TOTAL DO ESTOQUE', '='*30)
    print(f'||Total em unidades:{total_produtos}')
    print(f'||Valor total em estoque: R${valor_total:.2f}')

# função produto mais valia:


def ranking_valor_produto():

    if len(produtos) == 0:
        print('Não possui nenhum produto no estoque.')
        return

    produtos_ordenados = sorted(
        produtos,
        key=lambda produto: produto['preco'] * produto['quantidade'],
        reverse=True
    )

    mais_valioso = produtos_ordenados[0]

    print(f"O produto mais valioso é {mais_valioso['nome']}")
    print(
        f"Valor total: R$ {mais_valioso['preco'] * mais_valioso['quantidade']:.2f}")

# def menu


def menu():

    while True:
        print('\n' + '='*30)
        print('      SISTEMA DE ESTOQUE')
        print('='*30)
        print('1 - Cadastrar produto')
        print('2 - Mostrar produtos')
        print('3 - Ranking mais valioso')
        print('4 - Calcular estoque')
        print('5 - Sair')

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            cadastrar_produtos()

        elif opcao == 2:
            mostrar_produtos()

        elif opcao == 3:
            ranking_valor_produto()

        elif opcao == 4:
            calcular_estoque()

        elif opcao == 5:
            print('Encerrando sistema...')
            break

        else:
            print('Opção inválida.')


# main
menu()
