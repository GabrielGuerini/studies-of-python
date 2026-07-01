def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def multi(a, b):
    return a * b


def menu():
    print("""
===== MENU =====

1 - Divisão
2 - Multiplicação
3 - Subtração
4 - Soma
5 - Sair
""")


# Programa Principal
print("=" * 30, "Calculadora", "=" * 30)

while True:
    menu()

    opcao = int(input("Digite sua opção: "))

    if opcao == 5:
        print("Programa encerrado!")
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = div(a, b)
        print(f"Resultado: {resultado}")

    elif opcao == 2:
        resultado = multi(a, b)
        print(f"Resultado: {resultado}")

    elif opcao == 3:
        resultado = sub(a, b)
        print(f"Resultado: {resultado}")

    elif opcao == 4:
        resultado = soma(a, b)
        print(f"Resultado: {resultado}")

    else:
        print("Opção inválida!")