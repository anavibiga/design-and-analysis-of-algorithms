# Questão 15 - Testar se duas árvores binárias são similares

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sao_similares(raiz1, raiz2):
    # Se ambas as árvores são vazias, são similares
    if raiz1 is None and raiz2 is None:
        return True

    # Se uma das árvores é vazia e a outra não, não são similares
    if raiz1 is None or raiz2 is None:
        return False

    # Verifica se os nós atuais são iguais e verifica recursivamente as subárvores
    return (raiz1.val == raiz2.val) and \
           sao_similares(raiz1.left, raiz2.left) and \
           sao_similares(raiz1.right, raiz2.right)

# Árvore 1
print('\nDigite os dados da árvore 1:')
raiz1 = Node(input('Digite a raiz: '))
raiz1.left = Node(input('Digite a raiz-left: '))
raiz1.right = Node(input('Digite a raiz-right: '))
raiz1.left.left = Node(input('Digite a raiz-left-left: '))
raiz1.left.right = Node(input('Digite a raiz-left-right: '))
raiz1.right.left = Node(input('Digite a raiz-right-left: '))
raiz1.right.right = Node(input('Digite a raiz-right-right: '))

# Árvore 2
print('\nDigite os dados da árvore 2:')
raiz2 = Node(input('Digite a raiz: '))
raiz2.left = Node(input('Digite a raiz-left: '))
raiz2.right = Node(input('Digite a raiz-right: '))
raiz2.left.left = Node(input('Digite a raiz-left-left: '))
raiz2.left.right = Node(input('Digite a raiz-left-right: '))
raiz2.right.left = Node(input('Digite a raiz-right-left: '))
raiz2.right.right = Node(input('Digite a raiz-right-right: '))

# Resultados
if sao_similares(raiz1, raiz2):
    print('\nAs árvores são similares.')
else:
    print('\nAs árvores não são similares.')