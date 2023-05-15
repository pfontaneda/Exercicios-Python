from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
print('-=' * 12)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador ==0:
        print('EMPATE')
    elif jogador == 1:
        print('O jogador VENCE ')
    elif jogador == 2:
        print('O computador VENCE')
    else:
        print('\033[31mJogada Inválida')
elif computador == 1:
    if jogador ==0:
        print('O computador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O jogador VENCE')
    else:
        print('\033[31mJogada Inválida')
elif computador ==2:
    if jogador ==0:
        print('O jogador VENCE')
    elif jogador == 1:
        print('O computador VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\033[31mJogada Inválida')

