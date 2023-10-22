# Questão 10 - Inverter a ordem de uma lista encadeada

# Definindo a classe Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definindo a classe LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # Método para adicionar um novo nó com dados à lista
    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Método para inverter a lista
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Método para exibir os elementos da lista
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        # Retorna uma representação de string da lista
        return " -> ".join(elements) + " -> None"

# Criando a lista
my_list = LinkedList()
my_list.append(5)
my_list.append(10)
my_list.append(15)
my_list.append(20)

print('\nLista antes de ser invertida: ')
print(my_list)

# Invertendo a lista
my_list.reverse_list()

print('\nLista invertida: ')
print(my_list)