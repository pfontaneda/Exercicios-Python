num = (int(input('Digite um número:')),
       int(input('Digite outro número:')),
       int(input('Digite mais um número:')),
       int(input('Digite o último número número:')))
print(f'Vc digitou os números: {num}')
print(f'O número 9 foi digitado {num.count(9)} vezes')
if 3 in num:
       print(f'O número 3 foi digitado na posição {num.index(3)+1}')
else:
       print('O número 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')



