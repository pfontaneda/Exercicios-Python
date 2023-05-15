from random import randint
v =  0
print('--' * 20)
print('Vamos jogar PAR ou ÍMPAR')
print('--' * 20)
while True:
    jog = int(input('Digite um valor inteiro entre 0 e 10: '))
    comp = randint(0, 10)
    soma = jog + comp
    escolha = ' '
    while escolha not in ('PI'):
        escolha = str(input('par ou ímpar [P/I] ?')).strip().upper()[0]
    print(f'Vc jogou {jog} e o computador {comp}. O total foi {soma}, que é ')
    print('PAR' if soma % 2 == 0 else 'ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print("vc venceu!!")
            v += 1
        else:
            print('Vc perdeu!!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print("vc venceu!!")
            v += 1
        else:
            print('Vc perdeu!!')
            break
    print('Vamos jogar novamente ...')
print('--' * 20)
print(f'Game Over. Vc me venceu por {v} vezes!')
