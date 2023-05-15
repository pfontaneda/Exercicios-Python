from datetime import date
idade = int(input('Qual sua data de nascimento?'))
ano = date.today().year
if ano - idade <= 9:
    print('Vc tem {} anos e pode competir na categoria MIRIM'. format(ano - idade))
elif ano - idade <= 14:
    print('Vc tem {} anos e pode competir na categoria INFANTIL'.format(ano - idade))
elif ano - idade <= 19:
    print('Vc tem {} anos e pode competir na categoria JUNIOR'.format(ano - idade))
elif ano - idade == 20:
    print('Vc tem {} anos e pode competir na categoria SENIOR'.format(ano - idade))
else:
    print('Vc tem {} anos e pode competir na categoria MASTER'.format(ano - idade))


