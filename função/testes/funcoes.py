def OlaPessoa(nome):
    print(f'Olá, {nome}!')

OlaPessoa('Andre')

def dobro(numero):
    return numero * 2

print(dobro(5) + 2)

def multiplicaoDoisNumeros(a, b = 1):
    """ Multiplica dois Numeros """
    return a * b
print(multiplicaoDoisNumeros(3, 6))

x = 5 #variavel global
def soma():
    x = 10 #variavel local
    print (x)
    return x + 1
soma()
print(x)
