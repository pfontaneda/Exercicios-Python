def notas(*n, sit=False):
    """
    -> Função para analisar várias notas
    :param n: uma ou mais notas do aluno. Aceita várias
    :param sit: valor adicional indicando se deve ou não adicionar a situação do aluno
    :return: dicionário com várias informações sobre a nota do aluno
    """
    r = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
# help(notas)
# pode escrever os r linha por linha também
