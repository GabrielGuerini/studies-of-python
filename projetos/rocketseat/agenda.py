# Lista de contatos:
contatos = []

# Função cadastro.


def cadastrar_contato():

    nome = input('Digite o nome do contato: ')
    telefone = int(input('Digite o número: '))
    email = input('Digite o e-mail:')

    # Contato duplicado
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            print('Erro este contato já existe')
            contatos.remove(contato)
            print('Contato duplicado removido.')
            return
    # Dicionário.
    novo_contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'favorito': False
    }
    contatos.append(novo_contato)

    print('Cadastro de novo contato realizado!')
    voltar_menu()

# Função que converte o valor True/False em um emoji de favorito.
# Se favorito for True, retorna ⭐.
# Caso contrário, retorna ☆.


def favoritar_emoji(favorito):
    if favorito:
        return '⭐'
    return '☆'


def voltar_menu():
    input('\n🔙 Pressione Enter para voltar ao menu...')


# Nenhum contato cadastrado.
def nenhum_contato():
    if len(contatos) == 0:
        print('Nenhum contato cadastrado')
        return True

    return False

# def mostrar contatos em ordem alfábetica.


def mostrar_contato():

    if nenhum_contato():
        return

    # ordenar contatos pelo nome.
    contatos_ordenados = sorted(
        contatos,
        key=lambda contato: contato['nome'],
        reverse=False
    )

    for contato in contatos_ordenados:

        for contato in contatos_ordenados:

            print(f'''
            Nome: {contato['nome']} {favoritar_emoji(contato['favorito'])}
            Telefone: {contato['telefone']}
            E-mail: {contato['email']}
            {'=' * 30}
            ''')
        voltar_menu()

# def alterar dados do contato.


def alterar_dados():

    if nenhum_contato():
        return

    while True:
        print('''
|=====================================|
|        ⚙️ ALTERAR CONTATO ⚙️        |
|=====================================|
| 1 - 📞 Alterar número               |
|-------------------------------------|
| 2 - 📧 Alterar e-mail               |
|-------------------------------------|
| 3 - 🗑️ Remover contato             |
|-------------------------------------|
| 4 - ⭐ Alterar favoritos            |
|-------------------------------------|
| 5 - 🔙 Voltar ao menu              |
|=====================================|
''')
        opcao = int(input('Digite a opção: '))

        nome = input('Digite o nome do contato: ')

        # ALTERANDO NÚMERO:
        if opcao == 1:

            for contato in contatos:

                if contato['nome'].lower() == nome.lower():
                    novo_telefone = int(input('Digite o novo número: '))
                    contato['telefone'] = novo_telefone
                    print('Telefone alterado com sucesso!')
                    voltar_menu()

            print('Contato não encontrado.')
            voltar_menu()

        # ALterando e-mail:
        elif opcao == 2:

            for contato in contatos:

                if contato['nome'].lower() == nome.lower():
                    novo_email = input('Digite o novo e-mail: ')
                    contato['email'] = novo_email
                    print('E-mail alterado com sucesso!')
                    voltar_menu()

            print('Contato não encontrado.')
            voltar_menu()

        # Excluindo contato:
        elif opcao == 3:

            for contato in contatos:

                if contato['nome'].lower() == nome.lower():
                    print(f'Contato de {nome} encontrado!')
                    contatos.remove(contato)
                    print('Contato removido com sucesso!')
                    voltar_menu()

            print('Contato não encontrado.')
            voltar_menu()

        if opcao == 4:
            contato_favorito()

        elif opcao == 5:
            print('Voltando para o Menu.')
            break

        else:
            print('Opção não encontrada!')
            voltar_menu()
# ========================================================================================================


def buscar_contato():

    if nenhum_contato():
        return

    nome = input('Digite o nome do contato: ')

    for contato in contatos:

        if contato['nome'].lower() == nome.lower():

            print('Contato encontrado!')

            print(f'''
            =========================      
            Contato: {contato['nome']}{favoritar_emoji(contato['favorito'])}
            =========================
            Número: {contato['telefone']}
            =========================
            E-mail: {contato['email']}
            ========================= 
            ''')
            return

    print('Contato não encontrado.')


def contador_contatos():
    print(f' Total de contados: {len(contatos)}')

# ADIONAR OU REMOVER DOS FAVORTIOS.


def contato_favorito():
    while True:
        print('''
╔═════════════════════════════════════╗
║          ⭐ FAVORITOS ⭐            ║
╠═════════════════════════════════════╣
║ 1️⃣  📋 Mostrar favoritos           ║
║ 2️⃣  ⭐ Favoritar contato           ║
║ 3️⃣  ☆ Remover favorito            ║
║ 4️⃣  🔙 Voltar ao menu             ║
╚═════════════════════════════════════╝
''')

        opcao = int(input('Digite a sua escolha: '))

        if nenhum_contato():
            return

        if opcao == 1:
            for contato in contatos:

                if contato['favorito'] == True:
                    print(f'''
            =========================      
            Contato: {contato['nome']}
            =========================
            Favorito: {favoritar_emoji(contato['favorito'])}
            =========================
            ''')
        print('Você não possui contatos favoritos')

        if opcao == 2:

            nome = input('Digite o nome do contato que você quer favoritar: ')

            for contato in contatos:
                if contato['nome'].lower() == nome.lower():
                    contato['favorito'] = True
                    print('Contato favoritado!')

            print('Contato não encontrado.')

        elif opcao == 3:

            nome = input(
                'Digite o nome do contato que você deseja desfavoritar: ')

            for contato in contatos:
                if contato['nome'].lower() == nome.lower():
                    contato['favorito'] = False
                    print('Contato Removido dos favorito!')
                    voltar_menu()

            print('Contato não encontrado.')
            voltar_menu()

        elif opcao == 4:
            print('Voltando pro Menu.')
            break

        else:
            print('Opção não encontrado')
            voltar_menu()


def menu():
    while True:
        print('''
|=====================================|
|       📒 AGENDA DE CONTATOS 📒       |
|=====================================|
| 1 - ➕ Cadastrar contato            |
|-------------------------------------|
| 2 - 📋 Mostrar contatos             |
|-------------------------------------|
| 3 - 🔍 Buscar contato               |
|-------------------------------------|
| 4 - ⚙️ Alterar dados               |
|-------------------------------------|
| 5 - ⭐ Contatos favoritos          |
|-------------------------------------|
| 6 - 👤 Total de contatos           |
|-------------------------------------|
| 7 - 🚪 Sair                        |
|=====================================|
''')

        opcao = int(input('👉 Escolha uma opção: '))

        if opcao == 1:
            cadastrar_contato()

        elif opcao == 2:
            mostrar_contato()

        elif opcao == 3:
            buscar_contato()

        elif opcao == 4:
            alterar_dados()

        elif opcao == 5:
            contato_favorito()

        elif opcao == 6:
            contador_contatos()

        elif opcao == 7:
            print('\n👋 Encerrando a Agenda de Contatos...')
            break

        else:
            print('\n❌ Opção inválida. Tente novamente.')
