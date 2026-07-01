print('Bem-vindo ao Detran!')
print('Vamos verificar se você pode tirar a carteira de motorista.')
idade = int(input('Digite sua idade: '))
x = 18 - idade
if idade >= 18:
    print('Parabéns! Você pode tirar a carteira de motorista.')
else:
    print(f'Desculpe, você ainda não pode tirar a carteira de motorista. Aguarde mais {x} anos!')