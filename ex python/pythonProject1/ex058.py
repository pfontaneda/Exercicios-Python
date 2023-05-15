from random import randint
n = int(input('Eu pensei em um número entre 0 e 10, vc é capaz de adivinhar? Digite: '))
sorteio = randint(0,10)
tot = 1
while n != sorteio:
    n = int(input('Eu pensei em outro número, tente de novo: '))
    tot += 1
if n == sorteio:
    print('Parabéns, Eu pensei no número {} e vc acertou em {} tentativas'.format(sorteio, tot))
