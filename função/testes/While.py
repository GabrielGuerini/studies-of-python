#Toda repetição tem que ter um critério de parada, ou seja, uma condição que, quando satisfeita, fará com que a repetição pare. Caso contrário, teremos um loop infinito, ou seja, um ciclo que nunca termina.

soma = 0
n = 1

#Enquanto

while n <= 10:
    soma = soma + n
    n = n + 1

print(f' A soma dos números de 1 a 10 é: {soma}')

