gastos = []


# Função para cadastrar gastos ou receitas
def cadastrar_gastos():
    tipo = input('Digite o tipo (despesa/receita): ').lower()
    valor = float(input('Digite o valor: R$ '))
    categoria = input('Digite a categoria: ')

    novo_gasto = {
        'tipo': tipo,
        'valor': valor,
        'categoria': categoria
    }

    gastos.append(novo_gasto)
    print('Cadastro realizado com sucesso!')


# Função para mostrar os gastos
def mostrar_gastos():
    if len(gastos) == 0:
        print('Nenhum gasto cadastrado.')
        return

    print('\n===== SEUS GASTOS =====')

    for gasto in gastos:
        print(f'''
Tipo: {gasto["tipo"]}
Valor: R$ {gasto["valor"]:.2f}
Categoria: {gasto["categoria"]}
''')


# Função para mostrar o saldo
def mostrar_saldo():
    saldo = 0

    for gasto in gastos:
        if gasto['tipo'] == 'receita':
            saldo += gasto['valor']
        else:
            saldo -= gasto['valor']

    print(f'\nSeu saldo atual é: R$ {saldo:.2f}')


# Menu
def menu():
    print('''
===== MENU =====

1 - Cadastrar gasto
2 - Mostrar gastos
3 - Mostrar saldo
4 - Sair
''')


# Main
print('=' * 30, 'PLANO FINANCEIRO', '=' * 30)

while True:
    menu()

    opcao = input('Digite a opção: ')

    if opcao == '1':
        cadastrar_gastos()

    elif opcao == '2':
        mostrar_gastos()

    elif opcao == '3':
        mostrar_saldo()

    elif opcao == '4':
        print('Encerrando programa...')
        break

    else:
        print('Opção inválida! Tente novamente.')