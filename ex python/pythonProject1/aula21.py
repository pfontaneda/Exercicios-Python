# help() abre o promp e é só digitar a dúvida
# help(print) digita entre as chaves qual a dúvida
# print(input.__doc__) outro modo de ativar a função help, mas já em desuso

def contador(i, f, p):
    """
    faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='..')
        c += p
    print('FIM')


contador(2, 10, 2)


def somar(a=0, b=0, c=0):
    """
    faz a soma de três valores e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :função criada por mim para mim
    """
    s = a + b + c
    print(f'A soma é {s}')


somar(3, 2, 5)
somar(8, 4)
somar()


def teste():
    x = 8  # só vale esta variável aqui, pq está identada dentro da função
    print(f'Na função teste, o n vale {n}')
    print(f'Na função teste, o x vale {x}')


n = 2  # esta varíavel serve para os dois pq está fora da identação
teste()
print(f'No programa principal , o n vale {n}')


def teste1(b):
    global A
    A = 8
    b += 4
    c = 2
    print(f'A dentro vale {A}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


A = 5
teste1(A)
print(f'A fora vale {A}')


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'As somas foram: {r1}, {r2} e {r3}.')
