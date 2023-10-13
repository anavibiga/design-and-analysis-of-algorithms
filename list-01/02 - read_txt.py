# Exercicio 02 - Ler um texto de um arquivo do usuário e contar a quantidade de vogais

with open('texto.txt') as arquivo:
    texto = arquivo.read()

vogais = ['a', 'e', 'i', 'o', 'u']

c = 0

for i in texto:
    if i in vogais:
        c += 1

print('O texto é:\n{}'.format(texto))    
print('\nO total de vogais no texto é: {}.'.format(c))
