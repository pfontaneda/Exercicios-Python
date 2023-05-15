tot = totmil = menor = cont =  0
barato = ' '
print('--' * 15)
print('Xing Ling Store')
print('--' * 15)
while True:
    prod = str(input('Produto:')).strip()
    valor = float(input('valor: R$ '))
    cont += 1
    tot += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ?')).strip().upper()[0]
    print('--' * 20)
    if resp == 'N':
        break
print(f'O valor total da sua compra é de R${tot :.2f}')
print(f'Com {totmil} produtos custando mais de R$1000.00')
print(f'E o produto mais barato foi {barato} no valor de R$ {menor:.2f}')
