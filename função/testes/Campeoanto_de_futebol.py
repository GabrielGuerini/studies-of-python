print("=== Brasileirão de Futebol ===")
lista_times = []
nt = int(input('Digite a quantidade de times que participaram:'))
for i in range(nt):
    time = input(f"Digite o nome do time {i+1}: ")
    lista_times.append(time)
print("Os times participantes são:")
for time in lista_times:
    print(time)
tabela = []
for time in lista_times:
    vitórias = int(input(f'Quantas vitórias teve o {time}? '))
    empates = int(input(f'Quantos empates teve o {time}? '))
    derrotas = int(input(f'Quantas derrotas teve o {time}? '))
    pontos = (vitórias * 3) + empates
    linha = [time, vitórias, empates, derrotas, pontos]
    tabela.append(linha)
print(tabela)






