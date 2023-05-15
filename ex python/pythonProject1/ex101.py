def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Vc tem {idade} anos e não pode votar ainda'
    elif 16 <= idade < 18 or idade > 65:
        return f'Vc tem {idade} anos e seu voto é opcional'
    else:
        return f'Vc tem {idade} anos e seu voto é obrigatório'


print(voto(int(input('Em que ano vc nasceu?'))))




