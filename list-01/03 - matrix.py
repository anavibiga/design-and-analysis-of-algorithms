# Questão 03 - Função (e programa) que determina se uma matriz quadrada (n<100) é uma matriz de permutação
# matriz de permutação: composta por 0s e 1s, cada linha e coluna tem apenas um único valor 1

# Criando a função teste_matriz
def teste_matriz (matriz):
    # Limitando o tamanho da matriz
    len(matriz) <= 100
    # Certificando que a matriz é quadrada
    if len(matriz) != len(matriz[0]):
        return False
    # Certificando que a matriz é composta apenas de 0s e 1s
    for linha in matriz:
        for elemento in linha:
            if elemento != 0 and elemento != 1:
                return False
    # Checando se tem apenas um único 1 por linha e coluna
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

# Definindo uma matriz de teste
matriz1 =  [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]

# Checando se a matriz teste é uma matriz de permutação
if teste_matriz(matriz1) == True:
    print('A matriz satisfaz os requisitos de uma matriz de permutação.')
else:
    print('A matriz não satisfaz os requisitos de uma matriz de permutação.')