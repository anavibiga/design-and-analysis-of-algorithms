# Exercicio 03 - Função (e programa) que determina se uma matriz quadrada (n<100) é uma matriz de permutação
# matriz de permutação: composta por 0s e 1s, cada linha e coluna tem apenas um único valor 1

def teste_matriz (matriz):
    len(matriz) <= 100
    if len(matriz) != len(matriz[0]):
        return False
    for linha in matriz:
        for elemento in linha:
            if elemento != 0 and elemento != 1:
                return False
    for linha in matriz:
        if linha.count(1) != 1:
            return False
    for j in range(len(matriz)):
        count = 0
        for i in range(len(matriz)):
            count += matriz[i][j]
        if count != 1:
            return False        
    return True

matriz1 =  [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]


if teste_matriz(matriz1) == True:
    print('A matriz satisfaz os requisitos de uma matriz de permutação.')
else:
    print('A matriz não satisfaz os requisitos de uma matriz de permutação..')

