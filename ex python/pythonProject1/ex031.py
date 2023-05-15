d = float(input('Qual a distância da sua viagem em km?'))
if d <= 200:
    print('Para a distância de {:.1f} km , o valor da passagem é de: R${:.2f}'.format(d, (d*0.50)))
else:
    print('Para a distância de {:.1f} km , o valor da passagem é de: R${:.2f}'.format(d, (d*0.45)))



