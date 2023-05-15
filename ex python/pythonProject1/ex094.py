cadastro = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear() #tem q limpar os dados pra inserir novos dados
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['genero'] = str(input('Gênero [M/F]: ')).upper()[0]
        if pessoa['genero'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        resp = str(input('Quer cadastrar outra pessoa? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
# até aqui foi só alimentando dados. Agora q começam as análises
print('_-' * 20)
print(f'Ao todo foram cadastradas {len(cadastro)} pessoas')
media = soma / len(cadastro)
print(f'O grupo cadastrado tem {media:5.2f} anos em média')
print('Mulheres cadastradas: ', end='')
for p in cadastro:
    if p['genero'] in 'F':
        print(f'{p["nome"]}, ', end='')
print()
print ('Pessoas acima da idade média cadastrada:')
for p in cadastro:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'    {k} = {v}; ', end='')
        print()
print('Análise encerrada')
