def area(larg, comp):
    a = larg * comp
    print('--' * 20)
    print('Tamanho Terreno')
    print('--' * 20)
    print(f'A área do terreno {l} X {c} é de {a}m²')


l = float(input('largura do terreno em metros:'))
c = float(input('comprimento do terreno em metros:'))
area(l, c)
