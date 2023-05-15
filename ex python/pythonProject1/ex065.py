resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'S':
    n = int(input('Digite um número:'))
    soma += n
    quant += 1
    resp = str(input('Quer continuar [S/N] ?')).strip().upper()[0]
    if quant == 1 :
        maior = menor = n
    else:
        if n > maior :
            maior = n
        if n < menor:
            menor = n
media = soma / quant
print('Vc digitou {} números e a média foi {}'. format(quant, media))
print('Desses {} números, o maior foi {} e o menor {}'.format(quant, maior, menor))
