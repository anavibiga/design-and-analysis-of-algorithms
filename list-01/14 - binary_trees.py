# Questão 14 - Checar se uma árvore binária é (a) estritamente binária; (b) completa; ou (c) quase completa

# Definição da estrutura do nó da árvore binária
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

# Função para inserir um nó na árvore
def inserir_no(raiz, valor):
    if raiz is None:
        return Node(valor)
    if valor < raiz.value:
        raiz.left = inserir_no(raiz.left, valor)
    elif valor > raiz.value:
        raiz.right = inserir_no(raiz.right, valor)
    return raiz

# Função para verificar se uma árvore binária é estritamente binária, completa ou quase completa
def verificar_arvore(raiz):
    if raiz is None:
        return True, True, True
    
    fila = [(raiz, 1)]  # (nó, índice atual)
    total_nodes = 1
    ultimo_indice = 1
    nivel_atual = 1
    nivel_atual_nodes = 1
    
    estritamente_binaria = True
    completa = True
    
    while fila:
        no, indice = fila.pop(0)
        total_nodes = max(total_nodes, indice)
        
        # Verifica se o nó não tem exatamente 2 filhos
        if (no.left is not None and no.right is None) or (no.left is None and no.right is not None):
            estritamente_binaria = False
        
        if no.left:
            fila.append((no.left, 2 * indice))
            ultimo_indice = 2 * indice
            nivel_atual_nodes += 1
        if no.right:
            fila.append((no.right, 2 * indice + 1))
            ultimo_indice = 2 * indice + 1
            nivel_atual_nodes += 1
        
        # Verifica se o nível está completo
        if nivel_atual_nodes != 2 ** nivel_atual:
            completa = False
        
        # Move para o próximo nível
        if indice == 2 ** nivel_atual - 1:
            nivel_atual += 1
            nivel_atual_nodes = 0
    
    quase_completa = total_nodes == ultimo_indice + 1 and completa
    
    return estritamente_binaria, completa, quase_completa

# Árvore para teste
raiz = Node(input('Digite a raiz da árvore: '))
raiz.left = Node(input('Filho esquerda: '))
raiz.right = Node(input('Filho direita: '))
raiz.left.left = Node(input('Filho esquerda-esquerda: '))
raiz.left.right = Node(input('Filho esquerda-direita: '))
raiz.right.left = Node(input('Filho direita-esquerda: '))
raiz.right.right = Node(input('Filho direita-direita: '))

# Verificar a árvore
estritamente_binaria, completa, quase_completa = verificar_arvore(raiz)

# Mostrando a árvore
print('\nA árvore: ')
print('         {}'.format(raiz.value))
print('      /     \\')
print('   {}          {}'.format(raiz.left.value, raiz.right.value))
print(' /   \\       /  \\')
print('{}     {}    {}      {}'.format(raiz.left.left.value, raiz.left.right.value, raiz.right.left.value, raiz.right.right.value))

# Imprime os resultados
print('\nResultados: ')

print('\nEstritamente binária:', estritamente_binaria)
print('Completa:', completa)
print('Quase completa:', quase_completa)