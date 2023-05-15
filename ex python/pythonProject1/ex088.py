from random import randint
from time import sleep
lista = list()
jogos = list()
print('-_' * 20)
print('               MEGA SENA          ')
print('-_' * 20)
quant = int(input('Quantos jogos vc quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('-_' * 4, f'SORTEANDO {quant} JOGOS', '-_' * 4)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print()
print('_-' * 5, 'BOA SORTE!', '_-' * 5)

