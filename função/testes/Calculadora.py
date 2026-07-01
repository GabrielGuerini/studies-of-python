print("Olá! Bem-vindo ao programa de calculadora completa.")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
soma = float(n1) + float(n2)
print("A soma dos números é:", soma)
subtracao = float(n1) - float(n2)
print("A subtração dos números é:", subtracao)
multiplicacao = float(n1) * float(n2)
print("A multiplicação dos números é:", multiplicacao)
if float(n2) != 0:
    divisao = float(n1) / float(n2)
    print("A divisão dos números é:", divisao)      
else: 
    print("Não é possível dividir por zero.")