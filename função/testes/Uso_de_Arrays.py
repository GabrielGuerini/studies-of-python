#Array é uma estrutura que guarda vários valores em uma única variável.
#Em Python, os arrays são chamados de listas e são representados por colchetes [].
#Exemplo
notas = [9, 8, 7, 6.5, 5]

media = 0
for notas in notas:
    media += notas

media /= 5
print(f'A média das notas é: {media:.2f}')
