# Questão 05 - Busca em profundidade

from collections import defaultdict

# Grafo direcionado com lista de adjacência
class Grafo:
 
    def __init__(self):
        self.grafo = defaultdict(list)
 
    # Função para adicionar uma aresta ao grafo
    def adicionarAresta(self, u, v):
        self.grafo[u].append(v)
 
    # Função utilizada pelo DFS
    def DFSUtil(self, v, visitado):
        # Marca o nó atual como visitado e imprime
        visitado.add(v)
        print(v, end=' ')
 
        # Recorre a todos os vértices adjacentes a este vértice
        for vizinho in self.grafo[v]:
            if vizinho not in visitado:
                self.DFSUtil(vizinho, visitado)
 
    # A função para realizar a travessia DFS.
    def DFS(self, v):
        # Cria um conjunto para armazenar os vértices visitados
        visitado = set()
 
        # Chama a função auxiliar recursiva para imprimir a travessia DFS
        self.DFSUtil(v, visitado)
 

if __name__ == "__main__":
    g = Grafo()
    g.adicionarAresta(0, 1)
    g.adicionarAresta(0, 2)
    g.adicionarAresta(1, 2)
    g.adicionarAresta(2, 0)
    g.adicionarAresta(2, 3)
    g.adicionarAresta(3, 3)
 
    valor = int(input('Digite o ponto de partida: '))
    print('Segue a Travessia em Profundidade (começando do vértice {})'.format(valor))
     

# Chamada da função
g.DFS(valor)