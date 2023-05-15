cadastro = []
dados = []
peso = leve = 0
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        peso = leve = dados[1]
    else:
        if dados[1] > peso:
            peso = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    cadastro.append(dados[:])
    dados.clear() #tem q ficar aqui pra não somar os dados quando a lista rodar de novo no while.
    resp = str(input('Quer continuar ? [S/N]'))
    if resp in 'Nn':
        break
print(f'Foram adicionadas {len(cadastro)} pessoas')
print(f'O maior peso foi {peso} quilos, de ', end='')
for p in cadastro:
    if p[1] == peso:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi {leve} quilos, de ', end='')
for p in cadastro:
    if p[1] == leve:
        print(f'{p[0]}')
