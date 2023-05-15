def mensagem(msg):
    print('_-' * 20)
    print(msg)
    print('_-' * 20)


mensagem('Abobrinhas Voadoras')
mensagem('Cogumelos Hululantes')
mensagem('Maçãs Assassinas')


def soma(a, b):
    s = a + b
    print(s)


soma(4, 9)  # podemos mostrar dizendo qual é o parametro: soma(a=4, b=9) ou soma(b=4, a=9)
soma(6, 4)
soma(7, 2)


def mais(a, b):
    print(f'A = {a} e B = {b}')
    m = a + b
    print(f'A soma de A + B é {m}')


mais(3, 5)
mais(b=2, a=8)
mais(0, 2)


def contador(*num):  # vai criar tuplas pra cada parâmetro. Aí pode usar qualquer coisa de tupla
    print(num)
    for valor in num:
        print(f'{valor} ', end='')
    print('  Fim')
    tam = len(num)
    print(f'Recebi os valores {num} que são {tam} números')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(9, 5, 7, 6, 2, 4, 3, 1)


def dobra(lst):
    pos = 0  # posição
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 3, 5, 7, 9]  # lista
dobra(valores)
print(valores)
