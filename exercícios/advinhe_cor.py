print('------Bem vindo ao adivinhador de Cores--------')
input('Aperte enter quando estiver preparado...')
print('Feche os olhos, durante 10 segundos e pense numa cor')
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("A cor que você pensou foi Azul!")
