# Exercicio 01 - n (>1) primeiros primos dado um valor n (>0) dado pelo usuário

num = int(input('Diga o número inicial: '))

def primo(n):
    c = 1
    cdiv = 0
    while (c<=n):
        if (n%c == 0):
            cdiv += 1
        c += 1    
    if (cdiv == 2):
        print('{} é primo.'.format(n))

for i in range(num,0,-1):
    primo(i)
if (num <1):
    print('Tente novamente. O número inical precisa ser maior que 0.')
    




