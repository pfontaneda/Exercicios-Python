n1 = int(input('primeiro número:'))
n2 = int(input('segundo número:'))
n3 = int(input('terceiro número:'))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior número é:', maior)
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O menor número é', menor)
