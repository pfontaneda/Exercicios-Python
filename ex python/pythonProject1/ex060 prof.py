n = int(input('Fatorial de qual número?'))
count = n
f = 1
print('Calculando {}! = '.format(n), end = '')
while count > 0:
    print('{}'.format(count), end = '')
    print(' X ' if count > 1 else ' = ', end = '')
    f *= count
    count -= 1
print('{}'.format(f))
