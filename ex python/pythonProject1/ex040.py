nota1 = float(input('Qual sua primeira nota?'))
nota2 = float(input('Qual sua segunda nota?'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Sua média é {:.1f} e vc foi reprovado'.format(media))
elif 6.9 >= media >= 5.0:
    print('Sua média é {:.1f} e vc está de recuperação'.format(media))
elif media > 7.0:
    print('Sua média é {:.1f} e vc está aprovado, parabéns'.format(media))


    

