# Questão 11 - Criar duas pilhas dentro de um vetor

# Definindo a class Stacks
class Stacks:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.top1 = -1
        self.top2 = size
    
    # Método para adicionar valores na Pilha 1
    def push_1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = value
        elif self.top1 == self.top2 - 1 and self.top2 < self.size:
            self.top2 += 1
            self.array[self.top1] = value
        else:
            print('Estouro da pilha 1. Não é possível adicionar mais elementos.')

    # Método para adicionar valores na Pilha 2
    def push_2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = value
        elif self.top1 == self.top2 - 1 and self.top1 >= 0:
            self.top1 -= 1
            self.array[self.top2] = value
        else:
            print('Estouro da pilha 2. Não é possível adicionar mais elementos.')

    # Método para remover valores da Pilha 1
    def pop_1(self):
        if self.top1 >= 0:
            value = self.array[self.top1]
            self.top1 -= 1
            return value
        else:
            print('A pilha 1 está vazia.')
            return None

    # Método para remover valores da Pilha 2
    def pop_2(self):
        if self.top2 < self.size:
            value = self.array[self.top2]
            self.top2 += 1
            return value
        else:
            print('A pilha 2 está vazia.')
            return None

# Recebendo do usuário o tamanho total do vetor
size = int(input('Qual é o tamanho do vetor? '))
two_stacks = Stacks(size)

# Recebendo do usuário os dados da Pilha 1
size_stack_1 = int(input('\nQual é o tamanho da Pilha 1? '))

# Checando se os dados da Pilha 1 são factíveis
while (size_stack_1 > size-1):
    print('Não é possível ter uma pilha deste tamanho. O maior valor para a Pilha 2 é {}.'.format(size-1))
    size_stack_1 = int(input('\nDigite um novo valor pra Pilha 1: '))    

print('\nInsira os elementos para a Pilha 1: ')
for i in range(size_stack_1):
    # Pedindo os elementos da lista, utilizando i+1 porque a posição começa em 0
    elemento = input('{}º elemento da Pilha 1: '.format(i+1))
    two_stacks.push_1(elemento)

# Recebendo do usuário os dados da Pilha 2
size_stack_2 = int(input('\nQual é o tamanho da Pilha 2? '))

# Checando o valor máximo da Pilha 2
max_stack_2 = size - size_stack_1

while size_stack_2 > max_stack_2:
    print('Não é possível ter uma pilha deste tamanho. O maior valor para a Pilha 2 é {}.'.format(max_stack_2))
    size_stack_2 = int(input('\nDigite um novo tamanho para a Pilha 2: '))

print('\nInsira os elementos para a Pilha 2: ')
for i in range(size_stack_2):
    elemento = input('{}º elemento da Pilha 2: '.format(i + 1))
    two_stacks.push_2(elemento)

# Mostrando os elementos das pilhas
print('\nElementos da Pilha 1: ')
while True:
    elemento = two_stacks.pop_1()
    if elemento is None:
        break
    print(elemento)

print('\nElementos da Pilha 2: ')
while True:
    elemento = two_stacks.pop_2()
    if elemento is None:
        break
    print(elemento)