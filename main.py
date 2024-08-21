# nota do autor 

# forte ênfase nos comentários de código foi dada por mim nesse projeto, tanto a fins
# de visar a manutenibilidade e as boas práticas, quanto por fins de capricho e gosto pessoal.

# por mais que uma "modularização" em diferentes arquivos seria um padrão de projeto preferível,
# uma ambiguidade -- ou arguivelmente uma incapacidade da minha parte de compreender com clareza
# o enunciado do projeto -- na descrição do trabalho deu a mim o entendimento que um arquivo fonte
# unitário seria usado para testes que determinariam a avaliação daquele, e portanto decidi
# por assim fazê-lo. 

# em python, usamos snake_case.


# INÍCIO DO TRABALHO

import os # pra uso de comandos no terminal em funções diversas->(?)

# def mostra_titulo():  # função pra mostar o título (e uma "assinatura") da aplicação. foi removido pois o beecrowd quebra.
#   print(""" 
        
                                    
#                 ▄▄█████  ▐█████▄     ▐███         ██    ▄██
#                 ▐██████▀▀  ▐██▀███▌    █████       ▐███  █████
#                 ███▀       ▐██ ███▌    █████▌      ███████████
#                 ████▄▄     ▐██▐█████  ▐██▀███     ▐████████████
#                 ███████▄  ▐███▀▀███▌ ███▄████    ███ ████  ███▌
#                     ▀▀████  ██▌  ███▌ ████████▌  ███▌  █▀   ████
#                 ███     ███  ███▄████ ▐██▌   ███▌ ███        ▐███
#                 ███████████  ███████  ▐██     ██▌▐██▌         ███▌
#                 ▀▀▀▀▀▀▀▀▀   ▀▀▀▀     ▀▀▀     ▀▀▀▐██


#            ▄
#           ▀
# █▀█ ▀█▀ ▄▀█ █ █ █ █▀█   █▀ █▄▄ ▄▀█ █▀▄▀█ █▀█ ▄▀█ ▀█▀ █▀█   ▄▀█ █▄ █ █▀▄ █▀█ ▄▀█ █▀▄ █▀▀
# █▄█  █  █▀█ ▀▄▀ █ █▄█   ▄█ █▄█ █▀█ █ ▀ █ █▀▀ █▀█  █  █▄█   █▀█ █ ▀█ █▄▀ █▀▄ █▀█ █▄▀ ██▄
                                     
#                                 ▄█ █▀█ ▄▀█
#                                 ░█ █▄█ █▀█
# """)

def recebe_grafo(): # criador do grafo. cria um dicionário "grafo" e passa a ele todos os dados do objeto.
    funcoes = list(map(int, input().split()))  # selecionar as funções a executar
    n_vertices, n_arestas = map(int, input().split())  # separa a entrada em 2 info diferentes.
    direcionado = True if input() == 'direcionado' else False
    grafo = {i: [] for i in range(n_vertices)}  # para cada vértice no grafo criamos uma nova chave
    
    for _ in range(n_arestas):  # vamos pegar os dados para cada aresta
        id_aresta, u, v, peso = map(int, input().split())  # NECESSARIAMENTE respeitar a ordem numérica (0, 1...)
        grafo[u].append((v, peso, id_aresta))  # na chave do vértice u ("principal") adicionamos os valores do vértice com o qual ele se liga, a aresta que possibilita isso e o peso dessa.
        if not direcionado:  # caso o grafo não seja direcionado, criamos uma relação bidirecional.
            grafo[v].append((u, peso, id_aresta))   
            
    return funcoes, grafo, direcionado

def finaliza_programa(): # não é usada
   os.system("cls") # envia uma instrução ao terminal para que ele fique limpo.
   print("Programa finalizado.")

def mostra_dicionario(grafo):  # pra debugar, não é usada
   print(grafo)


def verifica_conexo(grafo):
    def dfs(vertice, visitados):
        visitados.add(vertice)
        for vizinho, _, _ in grafo[vertice]:
            if vizinho not in visitados:
                dfs(vizinho, visitados)

    if not grafo:
        return 1  # um grafo vazio é considerado conexo por definição

    primeiro_vertice = next(iter(grafo))
    visitados = set()
    dfs(primeiro_vertice, visitados)

    return 1 if len(visitados) == len(grafo) else 0
 
def verifica_bipartido(grafo):
    # func aux para fazer a (dfs) e verificar se o grafo é bipartido
    def dfs_bipartido(v, cor):
        cores[v] = cor # atribui a cor ao vértice atual
        for vizinho, _, _ in grafo[v]: # percorre os vizinhos do vértice atual
            if vizinho not in cores:
                if not dfs_bipartido(vizinho, not cor): # tenta colorir o vizinho com a cor oposta
                    return False # se falhar, o grafo não é bipartido
            elif cores[vizinho] == cor:
                return False # encontrou um vizinho com a mesma cor -> grafo não é bipartido
        return True # se todos os vizinhos puderem ser coloridos corretamente, retorna true

    cores = {} # dicionário para armazenar as cores dos vértices
    for vertice in grafo: # percorre todos os vértices do grafo
        if vertice not in cores: # se o vértice ainda não foi colorido
            if not dfs_bipartido(vertice, True): # começa a dfs tentando colorir o grafo
                return 0 # se falhar, retorna 0 (não bipartido)
    return 1 # se todos os vértices puderem ser coloridos, retorna 1 (bipartido)

def verifica_euleriano(grafo):
    def grau(v):
        return len(grafo[v])

    # verifica se o grafo é conexo
    if not verifica_conexo(grafo):
        return 0

    # verifica se todos os vértices têm grau par
    for v in grafo:
        if grau(v) % 2 != 0:
            return 0

    # se o grafo é conexo e todos os vértices têm grau par, é Euleriano
    return 1

def verifica_ciclo(grafo):
    # func auxiliar para fazer a (dfs) e verificar se há um ciclo
    def dfs_ciclo(v, pai):
        visitados.add(v) # marca o vértice atual como visitado
        for vizinho, _, _ in grafo[v]: # percorre os vizinhos do vértice atual
            if vizinho not in visitados:
                if dfs_ciclo(vizinho, v):
                    return True # se encontrar um ciclo em um vizinho, retorna true
            elif vizinho != pai:  # se encontrar um vizinho que não é o pai, é um ciclo
                return True
        return False # se não encontrou nenhum ciclo, retorna false

    visitados = set() # conjunto pra marcar os vértices visitados
    for vertice in grafo:
        if vertice not in visitados:
            if dfs_ciclo(vertice, None):
                return 1
    return 0 # se não encontrar nenhum ciclo, retorna 0

def lista_conexos(grafo, direcionado):
    
    if(direcionado == True):
        return '-1'  # retorna 1 se for orientado
    
    
    def dfs(v):
        visitados.add(v)
        for vizinho, _, _ in grafo[v]:
            if vizinho not in visitados:
                dfs(vizinho)

    visitados = set()
    componentes = 0
    for v in grafo:
        if v not in visitados:
            dfs(v)
            componentes += 1  # contador de componentes a cada nova componente encontrada

    return componentes

def lista_fortemente_conexos(grafo, direcionado):
    
    # verifica se o grafo é direcionado
    if not direcionado:
        return -1  # se não for, retorna -1
    
    # função para a primeira passagem do dfs
    def dfs_primeira_passagem(v):
        visitados.add(v)  # marca o vértice como visitado
        for vizinho, _, _ in grafo[v]:  # percorre os vizinhos do vértice atual
            if vizinho not in visitados:
                dfs_primeira_passagem(vizinho)  # chama o dfs pros os vizinhos
        ordem.append(v)  # adiciona o vértice à ordem de finalização

    # função para a segunda passagem do dfs
    def dfs_segunda_passagem(v, componente):
        visitados.add(v)  # marca o vértice como visitado
        componente.append(v)  # adiciona o vértice à componente atual
        for vizinho, _, _ in grafo_transposto[v]:  # percorre os vizinhos no grafo transposto
            if vizinho not in visitados:
                dfs_segunda_passagem(vizinho, componente)  # chama o dfs rec. pros vizinhos

    visitados = set()  # conjunto p marcar os vértices visitados
    ordem = []  # lista para armazenar a ordem de finalização dos vértices
    
    for v in grafo:  # pra percorrer todos os vértices do grafo
        if v not in visitados:
            dfs_primeira_passagem(v)  # executa a primeira passagem do dfs

    grafo_transposto = {v: [] for v in grafo}  # inicializa o grafo transposto
    for v in grafo:
        for vizinho, peso, id_aresta in grafo[v]:
            grafo_transposto[vizinho].append((v, peso, id_aresta))  # preenche o grafo transposto

    visitados.clear()  # limpa o conjunto de visitados p/ segunda passagem
    componentes = []  # lista para armazenar as componentes fortemente conexos
    for v in reversed(ordem):  # percorre os vértices na ordem inversa de finalização
        if v not in visitados:
            componente = []  # inicializa uma nova componente
            dfs_segunda_passagem(v, componente)  # executa a segunda passagem do dfs
            componentes.append(componente)  # adiciona a componente à lista de componentes

    return len(componentes)  # retorna o número de componentes fortemente conexas ->
    # -> (acredito que era essa a ideia)

def lista_uma_trilha_euleriana(grafo):
    # verifica se o grafo é euleriano
    if not verifica_euleriano(grafo):
        return '-1'
    
    # func para encontrar uma trilha euleriana usando dfs
    def dfs_euleriano(v):
        trilha = [] # lista para armazenar a trilha euleriana
        pilha = [v] # inicializa a pilha com o vértice de partida
        while pilha:
            v = pilha[-1] # pega o vértice do topo da pilha
            if grafo[v]: # verifica se o vértice ainda tem arestas não exploradas
                u, _, id_aresta = grafo[v].pop(0) # remove a primeira aresta do vértice
                for i, (w, _, _) in enumerate(grafo[u]):
                    if w == v: # encontra a aresta correspondente no vértice adjacente
                        del grafo[u][i] # remove a aresta correspondente no grafo
                        break
                pilha.append(u) # adc o próx. vertice
            else:
                trilha.append(pilha.pop()) # remove o vértice da pilha e adiciona à trilha
        return trilha[::-1] # retorna a trilha na ordem correta

    inicio = min(grafo.keys()) # encontra o vértice de início com a menor chave
    trilha = dfs_euleriano(inicio) # gera a trilha euleriana
    return ' '.join(map(str, trilha)) # retorna ela (como string de vértices)

def lista_vertices_de_articulacao(grafo, direcionado):
    # se o grafo é direcionado, não podemos encontrar vértices de articulação
    if direcionado:
        return -1;
    
    def dfs(v, pai, tempo):
        nonlocal tempo_descoberta, tempo_menor, filhos
        visitados.add(v)
        # marca o tempo de descoberta e o menor tempo de descoberta do vértice
        tempo_descoberta[v] = tempo_menor[v] = tempo
        tempo += 1
        filhos[v] = 0

        for vizinho, _, _ in grafo[v]:
            if vizinho not in visitados:
                filhos[v] += 1
                # faz a dfs no vizinho
                dfs(vizinho, v, tempo)
                # atualiza o menor tempo de descoberta
                tempo_menor[v] = min(tempo_menor[v], tempo_menor[vizinho])
                # se não for o pai e a menor descoberta do vizinho é maior ou igual
                # ao tempo de descoberta do vértice atual, é um vértice de articulação
                if pai is not None and tempo_menor[vizinho] >= tempo_descoberta[v]:
                    articulacoes.add(v)
            elif vizinho != pai:
                tempo_menor[v] = min(tempo_menor[v], tempo_descoberta[vizinho])

        # se v for a raiz e tiver mais de um filho, é um pt de articulação
        if pai is None and filhos[v] > 1:
            articulacoes.add(v)

    visitados = set()
    tempo_descoberta = {}
    tempo_menor = {}
    filhos = {}
    articulacoes = set()

    # realiza a busca em profundidade para encontrar os pontos de articulação (p retornar no fim)
    for v in grafo:
        if v not in visitados:
            dfs(v, None, 0)

    return ' '.join(map(str, sorted(articulacoes)))

def lista_arestas_ponte(grafo, direcionado):
    # verifica se o grafo é direcionado, pois o algoritmo é para grafos não direcionados
    if direcionado:
        return -1

    def dfs(v, pai, tempo):
        # realiza uma busca em profundidade para encontrar arestas de ponte
        nonlocal tempo_descoberta, tempo_menor
        visitados.add(v)  # marca o vértice como visitado
        tempo_descoberta[v] = tempo_menor[v] = tempo  # define o tempo de descoberta e menor como o tempo atual
        tempo += 1  # incrementa o tempo para os próximos vértices

        for vizinho, _, id_aresta in grafo[v]:
            if vizinho not in visitados:
                # se o vizinho não foi visitado, faz a chamada recursiva para ele
                dfs(vizinho, v, tempo)
                # atualiza o menor tempo de descoberta para o vértice v
                tempo_menor[v] = min(tempo_menor[v], tempo_menor[vizinho])
                # se a menor descoberta do vizinho é maior que a descoberta do vértice v, é uma aresta de ponte
                if tempo_menor[vizinho] > tempo_descoberta[v]:
                    pontes.add(id_aresta)
            elif vizinho != pai:
                # se o vizinho foi visitado e não é o pai, atualiza o menor tempo de descoberta
                tempo_menor[v] = min(tempo_menor[v], tempo_descoberta[vizinho])

    visitados = set()  # conjunto de vértices visitados
    tempo_descoberta = {}  # dicionário para armazenar o tempo de descoberta de cada vértice
    tempo_menor = {}  # dicionário para armazenar o menor tempo de descoberta
    pontes = set()  # conjunto para armazenar as arestas de ponte

    for v in grafo:
        if v not in visitados:
            # inicia a busca em profundidade a partir do vértice não visitado
            dfs(v, None, 0)

    return len(pontes)  # retorna o número de arestas de ponte encontradas

def gera_arvore_profundidade(grafo):
    def dfs(v):
        visitados.add(v)
        for vizinho, _, id_aresta in sorted(grafo[v], key=lambda x: x[0]):
            if vizinho not in visitados:
                arvore.append(id_aresta)
                dfs(vizinho)

    visitados = set()
    arvore = []
    dfs(0)
    return ' '.join(map(str, arvore))

def gera_arvore_largura(grafo):
    from collections import deque
    visitados = set()
    fila = deque([0])
    arvore = []
    visitados.add(0)

    while fila:
        v = fila.popleft()
        for vizinho, _, id_aresta in sorted(grafo[v], key=lambda x: x[0]):
            if vizinho not in visitados:
                arvore.append(id_aresta)
                visitados.add(vizinho)
                fila.append(vizinho)

    return ' '.join(map(str, arvore))

def gera_arvore_geradora_minima(grafo, direcionado):
    # retorna -1 se o grafo for direcionado, pois o algoritmo é para grafos não direcionados
    if direcionado:
        return '-1'
    
    def encontrar(pai, i):
        # encontra o representante do conjunto de i
        if pai[i] == i:
            return i
        return encontrar(pai, pai[i])

    def unir(pai, rank, x, y):
        # une os conjuntos de x e y
        raiz_x = encontrar(pai, x)
        raiz_y = encontrar(pai, y)
        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    arestas = []
    # coleta todas as arestas do grafo
    for v in grafo:
        for vizinho, peso, id_aresta in grafo[v]:
            if v < vizinho:  # evita duplicação de arestas
                arestas.append((peso, v, vizinho, id_aresta))
    # ordena as arestas por peso
    arestas.sort()

    pai = list(range(len(grafo)))  # inicializa o pai de cada vértice
    rank = [0] * len(grafo)  # inicializa o rank de cada vértice
    arvore = []  # lista para armazenar a árvore geradora mínima

    # constrói a árvore geradora mínima
    for peso, u, v, id_aresta in arestas:
        raiz_u = encontrar(pai, u)
        raiz_v = encontrar(pai, v)
        if raiz_u != raiz_v:
            arvore.append(id_aresta)  # adiciona o id da aresta à árvore
            unir(pai, rank, raiz_u, raiz_v)

    return ' '.join(map(str, arvore))  # retorna a árvore como uma string com os ids das arestas

def gera_ordem_topologica(grafo, direcionado):
    # verifica se o grafo é não direcionado
    if not direcionado:
        return -1 

    def dfs(v):
        nao_visitados.remove(v)
        visitados.add(v)
        ciclo_stack.add(v)
        
        for vizinho, _, _ in grafo[v]:
            if vizinho in ciclo_stack:
                return True  # ciclo detectado
            if vizinho in nao_visitados and dfs(vizinho):
                return True
        
        ciclo_stack.remove(v)
        ordem.append(v)
        return False

    nao_visitados = set(grafo.keys())
    visitados = set()
    ciclo_stack = set()
    ordem = []
    
    while nao_visitados:
        v = nao_visitados.pop()
        nao_visitados.add(v)
        if dfs(v):
            return -1  # retorna -1 se um ciclo for detectado

    return ' '.join(map(str, ordem[::-1]))

def gera_valor_caminho_minimo(grafo):
    # verifica se todos os pesos são iguais -> não-ponderado -> retorna -1
    pesos = set()
    for v in grafo:
        for _, peso, _ in grafo[v]:
            pesos.add(peso)
    if len(pesos) <= 1:
        return '-1'

    import heapq
    distancia = {v: float('inf') for v in grafo}
    distancia[0] = 0
    pq = [(0, 0)]

    while pq:
        dist, v = heapq.heappop(pq)
        if v == len(grafo) - 1:
            return str(dist)
        if dist > distancia[v]:
            continue
        for vizinho, peso, _ in grafo[v]:
            nova_dist = dist + peso
            if nova_dist < distancia[vizinho]:
                distancia[vizinho] = nova_dist
                heapq.heappush(pq, (nova_dist, vizinho))

    return '-1'

def gera_valor_fluxo_maximo(grafo, direcionado):
    # verifica se o grafo é não direcionado, pois o algoritmo é para grafos direcionados
    if not direcionado:
        return '-1'

    def bfs(s, t, pai):
        # realiza uma busca em largura para encontrar um caminho do source s ao target t
        visitados = set()
        fila = [s]
        visitados.add(s)
        pai[s] = -1  # inicializa o pai do source como -1

        while fila:
            u = fila.pop(0)  # remove o primeiro elemento da fila
            for v, capacidade, _ in grafo[u]:
                # se o vizinho v não foi visitado e a capacidade da aresta é positiva
                if v not in visitados and capacidade > 0:
                    fila.append(v)  # adiciona v à fila
                    visitados.add(v)  # marca v como visitado
                    pai[v] = u  # define o pai de v como u
                    if v == t:  # se o target t foi alcançado
                        return True
        return False

    s, t = 0, len(grafo) - 1  # define o source como 0 e o target como o último vértice
    pai = [-1] * len(grafo)  # inicializa a lista de pais com -1
    max_fluxo = 0  # inicializa o valor máximo do fluxo como 0

    while bfs(s, t, pai):
        # calcula o fluxo do caminho encontrado
        fluxo_caminho = float('inf')
        v = t
        while v != s:
            u = pai[v]
            # encontra a capacidade mínima ao longo do caminho
            for i, (vizinho, capacidade, _) in enumerate(grafo[u]):
                if vizinho == v:
                    fluxo_caminho = min(fluxo_caminho, capacidade)
                    break
            v = u

        max_fluxo += fluxo_caminho  # adiciona o fluxo do caminho ao fluxo máximo
        v = t
        while v != s:
            u = pai[v]
            # atualiza as capacidades das arestas no grafo
            for i, (vizinho, capacidade, _) in enumerate(grafo[u]):
                if vizinho == v:
                    grafo[u][i] = (vizinho, capacidade - fluxo_caminho, grafo[u][i][2])
                    break
            for i, (vizinho, capacidade, _) in enumerate(grafo[v]):
                if vizinho == u:
                    grafo[v][i] = (vizinho, capacidade + fluxo_caminho, grafo[v][i][2])
                    break
            v = u

    return str(max_fluxo)  # retorna o fluxo máximo como string

def gera_fecho_transitivo(grafo, direcionado):
    
    if not direcionado:
        return '-1'

    # faz o cálculo do fecho transitivo para grafos direcionados
    n = len(grafo)
    fecho = [[0 for _ in range(n)] for _ in range(n)]

    # inicializa a matriz de adjacência
    for v in grafo:
        fecho[v][v] = 1
        for vizinho, _, _ in grafo[v]:
            fecho[v][vizinho] = 1

    # algoritmo de floyd-warshall para fecho transitivo
    for k in range(n):
        for i in range(n):
            for j in range(n):
                fecho[i][j] = fecho[i][j] or (fecho[i][k] and fecho[k][j])

    # pegando os vértices alcançáveis a partir do vértice 0
    vertices_alcancaveis = [i for i in range(n) if fecho[0][i]]
    return ' '.join(map(str, sorted(vertices_alcancaveis)))

def executa_funcoes(funcoes, grafo, direcionado): # executador das funções
    for funcao in funcoes:
        if funcao == 0:
            print(verifica_conexo(grafo))
        elif funcao == 1:
            print(verifica_bipartido(grafo))
        elif funcao == 2:
            print(verifica_euleriano(grafo))
        elif funcao == 3:
            print(verifica_ciclo(grafo))
        elif funcao == 4:
            print(lista_conexos(grafo, direcionado))
        elif funcao == 5:
            print(lista_fortemente_conexos(grafo, direcionado))
        elif funcao == 6:
            print(lista_vertices_de_articulacao(grafo, direcionado))
        elif funcao == 7:
            print(lista_arestas_ponte(grafo, direcionado))
        elif funcao == 8:
            print(gera_arvore_profundidade(grafo))
        elif funcao == 9:
            print(gera_arvore_largura(grafo))
        elif funcao == 10:
            print(gera_arvore_geradora_minima(grafo, direcionado))
        elif funcao == 11:
            print(gera_ordem_topologica(grafo, direcionado))
        elif funcao == 12:
            print(gera_valor_caminho_minimo(grafo))
        elif funcao == 13:
            print(gera_valor_fluxo_maximo(grafo, direcionado))
        elif funcao == 14:
            print(gera_fecho_transitivo(grafo, direcionado))
        elif funcao == 15: # extra
            print(lista_uma_trilha_euleriana(grafo)) # extra

def main():
    funcoes, grafo, direcionado = recebe_grafo()
    executa_funcoes(funcoes, grafo, direcionado)

if __name__ == "__main__":
   main()
