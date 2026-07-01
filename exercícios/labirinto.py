import random


def criar_labirinto(tamanho):
    labirinto = [[random.randint(0, 1) for _ in range(tamanho)]
                 for _ in range(tamanho)]
    labirinto[0][0] = 8
    labirinto[tamanho - 1][tamanho - 1] = 9
    return labirinto


def exibir_labirinto(labirinto):
    for linha in labirinto:
        print(linha)


lab = criar_labirinto(5)
exibir_labirinto(lab)
