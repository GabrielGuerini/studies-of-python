# Empilhamento de dados (Stack)
# O último elemento a entrar é o primeiro a sair (LIFO)
# Last In, First Out (LIFO)


pilhas = []


def inserir():
    pilhas.append()


def remover():
    pilhas.pop()


inserir('prato A')
inserir('prato B')
inserir('prato C')
inserir('prato D')

print(pilhas)
remover()  # -> Vai ser removido o prato D
print(pilhas)
remover()  # -> removido prato C, assim adiante..
print(pilhas)
remover()
print(pilhas)
remover()
print(pilhas)

# insere o elemento x na posição 0, no topo!


def visitar(x):
    pilhas.insert(0, x)

# Remove o item na posição 0 ou seja elemento do topo.


def voltar():
    pilhas.pop(0)


visitar('Google')
visitar('Kabum')
visitar('Mostruario placa de video')
visitar('Pagamento placa de video')

# Como basicamente o voltar do navegador funciona.
print(pilhas)  # -> ultima pagina acessada, pagamento da placa de video.
voltar()
print(pilhas)
voltar()
print(pilhas)
voltar()
print(pilhas)
voltar()  # -> Primeira pagina acessado começo google
print(pilhas)
