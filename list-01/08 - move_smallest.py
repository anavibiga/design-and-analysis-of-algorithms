# Questão 08 - Encontrar o menor elemento da lista e mover pra primeira posição

# Definindo a classe Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definindo a classe LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # Método para adicionar um novo nó
    def append(self, data):
       new_node = Node(data)
       new_node.next = self.head
       self.head = new_node 

    # Método para mover o menor elemento para o início da lista
    def move_smallest_to_front(self):
        if self.head is None:
            return  
        
        prev = None
        current = self.head
        min_node = self.head
        prev_min = None

        # Encontrando o menor elemento na lista
        while current.next:
            if current.next.data < min_node.data:
                min_node = current.next
                prev_min = current

            current = current.next

        # Removendo o menor elemento de sua posição original
        if prev_min:
            prev_min.next = min_node.next
            # Movendo o menor elemento para o início da lista
            min_node.next = self.head
            self.head = min_node

    # Método para exibir os elementos da lista
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ') 
            current = current.next
        print('None')

# Recebendo os números do usuário
a = int(input('Adicione um número na lista: '))
b = int(input('Adicione um número na lista: '))
c = int(input('Adicione um número na lista: '))
d = int(input('Adicione um número na lista: '))

# Criando a lista encadeada
lista = LinkedList()
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)

print('\nLista original: ')
lista.display()

# Levando o menor elemento para o início da lista
lista.move_smallest_to_front()

print('\nLista após mover o menor elemento para o início: ')
lista.display()