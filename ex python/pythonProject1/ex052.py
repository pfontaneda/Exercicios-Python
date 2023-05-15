num = int(input('Digite um número:'))
contador = 0 #o número de divisíveis
for c in range (1, num + 1):
    if num % c == 0: #se o numero for divisivel pelo c
        contador += 1
if contador == 2: #o número é divisivel só 2 X . por um e por ele mesmo
    print('O número {} é PRIMO'.format(num))
else:
    print('O número {} NÂO é primo'.format(num))
