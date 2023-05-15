sal = float(input('Qual o seu salário?'))
if sal <= 1250:
    print('Vc teve aumento de 15% e seu salário atual será de: R$ {:.2f}'.format(sal+(sal*15/100)))
else:
    print('Vc teve aumento de 10% e seu salário atual será de: R$ {:.2f}'.format(sal+(sal*10/100)))



