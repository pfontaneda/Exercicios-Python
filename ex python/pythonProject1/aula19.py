pessoas = {'nome': 'Patricia', 'sexo': 'F', 'idade': 48}
print(pessoas)
print(pessoas['nome'])
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos')
# se já tem aspas simples referenciando a estrutura, tem q colocar aspas duplas pra declarar
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys(): #pra cada uma das chaves, mostrar:
    print(k)
for k , v in pessoas.items(): #aqui tem q colocar o k para keys e o v para values para ele pegar as duas informações
    print(f'{k} = {v}')
pessoas['nome'] = 'Doroteia'
for k , v in pessoas.items():
    print(f'{k} = {v}')
pessoas['peso'] = 46.7
for k , v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
for k , v in pessoas.items():
    print(f'{k} = {v}')
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1])
print(brasil[0]['uf'])
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil: #pra cada estado in brasil, mostre estado
    print(e)
for e in brasil: # este for é para a lista
    for k, v in e.items():  # este for pra dentro é do dicionário
        print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v, end = ' ')
    print()


