n = 1
while n != 0:
    n = int(input('Digite um número:'))
print('fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? S/N: ')).upper()
print('FIM')

a = 1
par = impar = 0
while a != 0:
    a = int(input('Digite um número inteiro:'))
    if a != 0: # assim o zero não entra na soma dos pares
        if a % 2 == 0:
            par += 1
        else:
            impar +=1
print('Vc digitou {} números pares e {} números ímpares'.format(par, impar))
