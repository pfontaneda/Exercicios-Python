s = 0
for c in range(1, 7):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        s += n
if s != 0:
    print('A soma dos números pares digitados é : {}'.format(s))
else:
    print('Não há números pares a serem somados')
