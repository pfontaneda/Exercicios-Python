boletim = list()
while True:
    nome = str(input('Nome: '))
    not1 = float(input('Nota 1: '))
    not2 = float(input('Nota 2: '))
    media = (not1 + not2) / 2
    boletim.append([nome, [not1, not2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-_' * 20)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 20)
for i, a  in enumerate(boletim):  # Indice, Aluno
    print(f'{i:<5}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 20)
    opc = int(input('Quer ver as notas de qual aluno? [999 finaliza]'))
    if opc == 999:
        break
    if opc <= len(boletim) - 1 :
        print(f'As notas de {boletim[opc][0]} : {boletim[opc][1]}')




