num= []
while True:
    num.append(int(input('Digite um número:')))
    resp = str(input('Quer continuar [S/N] ?')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Vc digitou {len(num)} números.')
num.sort(reverse=True)
print(f'Os números digitados em ordem decrescente foram: {num}')
if 5 in num:
    print('O número 5 faz parte da lista digitada')
else:
    print('Não foi digitado o número 5 na lista')
