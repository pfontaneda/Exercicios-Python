num = list()
while True:
    n = int(input('Digite um número:'))
    if n not in num:
        num.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado. Não será adicionado...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
print('-_' * 30)
num.sort()
print(f'Vc adicionou os números: {num}')
