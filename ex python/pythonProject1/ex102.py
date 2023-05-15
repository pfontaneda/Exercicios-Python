def fatorial(n, show=False):
    """
    Calcula o fatorial de um número e se quer detalhado ou não como opcional
    :param n: o número a ser calculado
    :param show: a opção de detalhar ou não
    :return: o valor fatorial de um número n
    """
    from math import factorial
    if show:
        f = 1
        for c in range(n, 0, -1):
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
            f *= c
        return f
    else:
        f = factorial(n)
        return f'O fatorial de {n} é {f}'


print(fatorial(int(input('Fatorial de qual número? ')), (bool(input('Quer mostrar detalhado? [True/False] ')))))

