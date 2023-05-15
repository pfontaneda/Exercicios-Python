times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
           'Flamengo', 'Atlético PR', 'Atlético MG', 'Fortaleza',
           'São Paulo', 'América MG', 'Botafogo', 'Santos',
           'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
           'Ceará SC', 'Atlético GO', 'Avaí', 'Juventude')
print('=-' * 20)
print('{:^40}'.format('BRASILEIRÃO 2022'))
print('=-' * 20)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O time Santos ocupa a posição : {times.index("Santos")+1}')


