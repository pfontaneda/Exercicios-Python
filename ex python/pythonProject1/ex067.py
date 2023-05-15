n = 0
while True:
    n = int(input('Tabuada do número: '))
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} * {c} = {n*c}')
print('_' * 12)
print('Programa encerrado')