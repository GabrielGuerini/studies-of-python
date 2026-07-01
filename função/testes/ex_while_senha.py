#Pedindo a senha correta usando while

senha = ("Zeus")
us = input('Digite a senha: ')

while us != senha:
    print("Você errou a senha")
    us = input('Digite a senha novamente: ')
print('Você acertou a senha')


    