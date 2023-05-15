n1 = float(input('Digite sua nota:'))
n2 = float(input('Digite sua outra nota:'))
m = (n1 + n2)/2
if m >= 6.0:
    print('Sua média é {:.1f} , PARABENS!'.format(m))
else:
    print('Sua média é {:.1f} , precisa estudar mais'.format(m))


