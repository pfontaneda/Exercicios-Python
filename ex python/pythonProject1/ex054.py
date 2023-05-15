from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Qual sua data de nascimento?'))
    idade = atual - nasc
    if idade < 21:
        totmenor += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E {} pessoas menores de idade'.format(totmenor))
