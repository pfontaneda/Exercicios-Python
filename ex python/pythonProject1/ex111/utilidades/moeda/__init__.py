def aumentar(preco=0, taxa=0, forma=False):
    """
    Calcula o aumento de determinado preço,
    retornando o resultado com ou sem formatação
    :param preco: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento
    :param forma: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    resp = preco + (preco * taxa / 100)
    return resp if forma is False else moeda(resp)


def diminuir(preco=0, taxa=0, forma=False):
    resp = preco - (preco * taxa / 100)
    return resp if not forma else moeda(resp)


def dobro(preco=0, forma=False):
    resp = preco * 2
    return resp if not forma else moeda(resp)


def metade(preco=0, forma=False):
    resp = preco / 2
    return resp if not forma else moeda(resp)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=20, taxar=12):
    print('_' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('_' * 30)
    print(f'Valor analisado: \t{moeda(preco)}')
    print(f'O seu dobro: \t\t{dobro(preco, True)}')
    print(f'A sua metade: \t\t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: {aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de desconto: {diminuir(preco, taxar, True)}')
    print('_' * 30)
