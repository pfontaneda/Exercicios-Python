lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número:')))
    resp = str(input('Quer continuar [S/N] ?')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 ==0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
