
m = int(input('Digite um número para inserir na lista: '))
n = int(input('Digite outro número para inserir na lista: '))

# Definindo a classe Node
class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

# Definindo a classe LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # Método para inserir no início da lista
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Método para trocar dois nós consecutivos
    def swap_nodes(self, x, y):
        if x == y:
            return

        prev_x = None
        curr_x = self.head
        while curr_x and curr_x.data != x:
            prev_x = curr_x
            curr_x = curr_x.next

        prev_y = None
        curr_y = self.head
        while curr_y and curr_y.data != y:
            prev_y = curr_y
            curr_y = curr_y.next

        if not curr_x or not curr_y:
            # Um dos elementos não foi encontrado na lista
            return

        if prev_x:
            prev_x.next = curr_y
        else:
            self.head = curr_y

        if prev_y:
            prev_y.next = curr_x
        else:
            self.head = curr_x

        curr_x.next, curr_y.next = curr_y.next, curr_x.next

    # Método para representar a lista como uma string
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        result.append('None')
        return ' -> '.join(map(str, result))

# Criando uma instância da lista encadeada
my_list = LinkedList()

# Inserindo itens na lista
my_list.insert_at_beginning(5)
my_list.insert_at_beginning(m)
my_list.insert_at_beginning(n)
my_list.insert_at_beginning(15)

# Imprimindo a lista antes da troca
print('\nLista antes da troca: ')
print(my_list)

# Trocando dois nós consecutivos
my_list.swap_nodes(m, n)

# Imprimindo a lista após a troca
print('\nLista após a troca: ')
print(my_list)
