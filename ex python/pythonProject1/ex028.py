from random import randint
n = int(input('Eu pensei em um número, vc é capaz de advinhar?'))
sorteio = randint(0,5)
if n == sorteio:
    print('Parabéns, vc acertou!!')
else:
    print('Que pena, não foi desta vez. Eu pensei no {}'.format(sorteio))



