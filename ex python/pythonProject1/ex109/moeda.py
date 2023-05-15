def aumentar(preco=0, taxa=0, forma=False):
    resp = preco + (preco * taxa / 100)
    return resp if forma is False else moeda(resp)


def diminuir(preco=0, taxa=0, forma=False):
    resp =  preco - (preco * taxa / 100)
    return resp if not forma else moeda(resp)

def dobro(preco=0, forma=False):
    resp =  preco * 2
    return resp if not forma else moeda(resp)


def metade(preco=0, forma=False):
    resp = preco / 2
    return resp if not forma else moeda(resp)


def moeda(preco=0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
