# Questão 04 - Busca binária (recursiva e não recursiva) e análise de tempo de execução de pior caso

## Binary Search não recursivo

# Definindo a função de busca binária
def binary_search(list, item):
    high = len(list) - 1
    low = 0
    
    # Fazendo a "divisão" da lista para buscar o número desejado
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    # Item não encontrado, retornar -1
    return -1

# Obtendo o número do usuário
item = int(input('Qual número você quer encontrar? '))

# Definindo a lista
list = [1, 3, 5, 7, 9]

# Mostrando os resultados
result = binary_search(list, item)

# Tratamento de erro
if result != -1:
    print('O item {} foi encontrado na posição {}.'.format(item, result))
else:
    print('O item {} não consta na lista.'.format(item))
    

## Binary Search recursivo

item = int(input('Qual número você quer encontrar? '))

list = [1, 3, 5, 7, 9]

# Criando função da busca binária
def binary_search(list, item, low, high):
    if low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        # Checando se o item está acima ou abaixo da metade da lista ordenada
        if guess == item:
            return mid
        elif guess > item:
            return binary_search(list, item, low, mid - 1)
        else:
            return binary_search(list, item, mid + 1, high)
    else:
        return None

# Mostrando os resultados
result = binary_search(list, item, 0, len(list) - 1)

# Tratamento de erro
if result is not None:
    print('O item {} foi encontrado na posição {}.'.format(item, result))
else:
    print('O item {} não consta na lista.'.format(item))