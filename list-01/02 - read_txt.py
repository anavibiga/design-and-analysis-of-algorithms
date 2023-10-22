# Questão 02 - Ler um texto de um arquivo do usuário e contar a quantidade de vogais

# Abrindo o arquivo de texto
with open('texto.txt') as arquivo:
    texto = arquivo.read()
    texto = texto.lower()

# Definindo o que são vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# Definindo o contador de vogais
c = 0

# Procurando as vogais no texto
for i in texto:
    if i in vogais:
        c += 1

# Mostrando os resultados
print('O texto é:\n{}'.format(texto))    
print('\nO total de vogais no texto é: {}.'.format(c))