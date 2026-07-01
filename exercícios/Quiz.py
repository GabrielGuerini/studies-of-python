print('=' * 30, '🧠Bem-vindo ao jogo de perguntas e respostas🙈', '=' * 30)
print('Para cada pergunta que você acertar, você soma um ponto!💯')

perguntas = [
    ['Qual animal gosta muito de banana? ', 'Macaco'],
    ['Qual o maior jogador atual da seleção de Portugal? ', 'Cristiano Ronaldo'],
    ['Qual o maior jogador da Argentina atualmente? ', 'Messi'],
    ['Qual o animal com o maior pescoço? ', 'Girafa']
]
comecar = input('Você está pronto para começar? Digite S para SIM ou N para NÃO: ').lower()
while comecar == 's':
    print('⏲️ Contagem regressiva de 5 segundos...')
    import time
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    break
input('Pressione ENTER para a primeira pergunta: ')
pontos = 0
for pergunta in perguntas:
    resposta = input(pergunta[0]).lower()

    if resposta == pergunta[1].lower():
        print('✅ Acertou!')
        pontos += 1
    else:
        print(f'❌ Errou! A resposta correta era: {pergunta[1]}')
print('\n🏆 Fim do jogo!')
print(f'Você fez {pontos} de {len(perguntas)} pontos.')