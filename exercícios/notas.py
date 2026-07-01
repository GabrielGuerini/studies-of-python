def aprovado(media):
    if media >= 6:
        print('Aprovado')
    else:
        print('Reprovado')


def calMedia(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4


def notas():
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    nota3 = float(input('Digite sua terceira nota: '))
    nota4 = float(input('Digite sua quarta nota: '))
    return nota1, nota2, nota3, nota4


# main
nota1, nota2, nota3, nota4 = notas()
media = calMedia(nota1, nota2, nota3, nota4)
aprovado(media)
