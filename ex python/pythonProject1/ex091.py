from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = [] #será uma lista com 4 tuplas
print('VALORES SORTEADOS')
print('_-' * 20)
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('_-' * 20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #é assim q coloca do maior pro menor
for i, v in enumerate(ranking):
    print(f'{i +1}o lugar: {v[0]} com {v[1]} ')
    sleep(1)
print('_-' * 20)



