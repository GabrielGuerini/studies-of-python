# n = 1 > [ 1 ] = 1
# n = 2 > [ 1, 1], [ 2 ] = 2
# n = 3 > [ 1, 1, 1 ], [ 1, 2 ], [ 2, 1 ] = 3
# n = 4 > [ 1, 1, 1, 1 ], [ 2, 1, 1 ], [ 1, 2, 1 ], [ 1, 1, 2 ] [ 2, 2 ] = 5
# n = 5 > 8

def contar_caminhos(num_pedras):
    if num_pedras <= 1:
        return 1
    # else recursivo.
    return contar_caminhos(num_pedras - 1) + contar_caminhos(num_pedras - 2)


print(contar_caminhos(4))
