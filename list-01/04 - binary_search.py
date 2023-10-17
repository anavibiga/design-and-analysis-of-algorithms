# Binary Search não recursivo

item = int(input('Qual número você quer encontrar? '))

list = [1, 3, 5, 7, 9]

def binary_search(list, item):
    high = len(list) - 1
    low = 0
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        
        if guess == item:
            print('O item {} foi encontrado na posição {}.'.format(item, mid))
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    print('O item {} não consta na lista.'.format(item))
    return None

binary_search(list, item)



