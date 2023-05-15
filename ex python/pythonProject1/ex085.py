lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}o. número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('_-' * 30)
lista[0].sort()
lista[1].sort()
print(f'Os números pares digitados em ordem foram: {lista[0]}')
print(f'Os números ímpares digitados em ordem foram: {lista[1]}')

