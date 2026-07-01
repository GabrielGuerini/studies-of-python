# é uma forma de navegar nas listas usando alguma forma, exemplo a baixo:
# conseguimos vizualisar separadamente quantas letras tem cada nome
# separa a lista de acordo com uma função

nomes = [
    'João',
    'Antonio',
    'Gabriel',
    'Mario',
    'Harry',
    'Lenon'
]

tabela = {}

for nome in nomes:
    qtd = nome[0]
    if qtd not in tabela:
        tabela[qtd] = []
    tabela[qtd].append(nome)

print(tabela)
