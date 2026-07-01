import heapq

# 1. Criamos uma lista comum que servirá como nossa Heap
fila_clientes = []

# 2. Função para adicionar cliente (Armazenar na Heap)


def adicionar_cliente(lista_heap, nome, prioridade):
    # Armazenamos como uma tupla: (prioridade, nome)
    # O heapq vai organizar a lista automaticamente com base na prioridade
    heapq.heappush(lista_heap, (prioridade, nome))
    print(f"Cliente '{nome}' adicionado com prioridade {prioridade}.")

# 3. Função para remover o cliente de maior prioridade (remover explicitamente)


def remover_proximo_cliente(lista_heap):
    if not lista_heap:
        print("A fila está vazia!")
        return None

    # O heappop remove e retorna o elemento com a MENOR numeração de prioridade (ex: 1)
    prioridade, nome = heapq.heappop(lista_heap)
    print(f"--> Removendo cliente: {nome} (Prioridade: {prioridade})")
    return nome

# --- TESTANDO O FLUXO ---


# Adicionando clientes em ordem aleatória de chegada
adicionar_cliente(fila_clientes, "Carlos Silva", 3)
adicionar_cliente(fila_clientes, "Ana Souza", 1)  # Prioridade máxima
adicionar_cliente(fila_clientes, "Bruno Lima", 2)

print("\nEstado atual da lista interna (organizada como árvore/heap):", fila_clientes)
print("-" * 50)

# O cliente só sai da lista quando chamamos a remoção explícita
print("\nChamando as remoções:")
remover_proximo_cliente(fila_clientes)  # Deve sair a Ana Souza (Prioridade 1)
remover_proximo_cliente(fila_clientes)  # Deve sair o Bruno Lima (Prioridade 2)
# Deve sair o Carlos Silva (Prioridade 3)
remover_proximo_cliente(fila_clientes)
