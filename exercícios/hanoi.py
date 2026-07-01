def mover_disco(num_discos, origem, destino, auxiliar):
    if num_discos == 1:
        print(f'Mover disco 1 da {origem} para {destino}')
    else:
        mover_disco(num_discos - 1, origem, auxiliar, destino)
        print(f'Mover disco {num_discos} da {origem} para {destino}')
        mover_disco(num_discos - 1, auxiliar, destino, origem)


mover_disco(3, 'Torre 1', 'Torre 3', 'Torre 2')
