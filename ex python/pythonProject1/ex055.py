maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual seu peso?'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {} kg'.format(maior))
print('E o menor peso lido foi de {} kg'.format(menor))