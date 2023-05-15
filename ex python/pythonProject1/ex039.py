from datetime import date
sexo = int(input('Qual seu gênero? Digite 1 para feminino e 2 para masculino:'))
if sexo == 1:
    print('Vc não tem a obrigação do alistamento militar')
elif sexo == 2:
    nasc = int(input('Qual a data do seu nascimento?'))
    atual = date.today().year
    idade = atual - nasc
    if idade < 18:
        saldo = 18 - idade
        print('Faltam ainda {} anos para vc se alistar'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade == 18:
        print('É hora de vc se alistar')
    elif idade > 18:
        saldo = idade - 18
        print('Vc passou {} anos do prazo de alistamento'.format(saldo))
        ano = atual - saldo
        print('Vc deveria ter se alistado em {}'.format(ano))




