from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 números...', end='')
    for cont in range(0, 5):
        n = randint(1, 50)
        lista.append(n)
        print(f'{n}, ', end='')
        sleep(0.5)
    print('PRONTO')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando só os valores pares, temos {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)
