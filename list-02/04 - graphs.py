# Questão 04 - Operações com Grafos

class GrafoMatrizAdjacencias:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]

    def adicionar_aresta(self, vertice_origem, vertice_destino):
        self.matriz[vertice_origem][vertice_destino] = 1
        self.matriz[vertice_destino][vertice_origem] = 1

    def vizinhos(self, vertice):
        return [v for v, adj in enumerate(self.matriz[vertice]) if adj == 1]

    def testar_vizinhanca(self, vertice1, vertice2):
        return self.matriz[vertice1][vertice2] == 1

    def remover_aresta(self, vertice_origem, vertice_destino):
        self.matriz[vertice_origem][vertice_destino] = 0
        self.matriz[vertice_destino][vertice_origem] = 0

class GrafoListaAdjacencias:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, vertice_origem, vertice_destino):
        self.lista[vertice_origem].append(vertice_destino)
        self.lista[vertice_destino].append(vertice_origem)

    def vizinhos(self, vertice):
        return self.lista[vertice]

    def testar_vizinhanca(self, vertice1, vertice2):
        return vertice2 in self.lista[vertice1]

    def remover_aresta(self, vertice_origem, vertice_destino):
        self.lista[vertice_origem].remove(vertice_destino)
        self.lista[vertice_destino].remove(vertice_origem)

# Criando um grafo com 5 vértices
grafo_matriz = GrafoMatrizAdjacencias(5)

# Adicionando arestas
grafo_matriz.adicionar_aresta(0, 1)
grafo_matriz.adicionar_aresta(0, 2)
grafo_matriz.adicionar_aresta(1, 3)
grafo_matriz.adicionar_aresta(2, 4)

# Mostrando a matriz de adjacências
for linha in grafo_matriz.matriz:
    print(linha)
    
# Criando um grafo com 5 vértices
grafo_lista = GrafoListaAdjacencias(5)

# Adicionando arestas
grafo_lista.adicionar_aresta(0, 1)
grafo_lista.adicionar_aresta(0, 2)
grafo_lista.adicionar_aresta(1, 3)
grafo_lista.adicionar_aresta(2, 4)

# Mostrando a lista de adjacências
for i, vizinhos in enumerate(grafo_lista.lista):
    print('Vértice {}: {}'.format(i,vizinhos))