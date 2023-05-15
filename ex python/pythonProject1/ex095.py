time = []
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for c in range(0, tot):
        gols.append(int(input(f'   Quantos gols na {c +1}o partida? ')))
    jogador['totgol'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy()) #jogador é dicionário
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
print('_-' * 20)
print(' COD  ', end='')
for i in jogador.keys():
    print(f'{i:<13}', end='')
print()
for k, v in enumerate(time): #time é lista
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_-' * 20)
while True:
    busca = int(input('Buscar dados de qual jogador? 999 para encerrar '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!! Não existe jogador com o código {busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['totgol']): #indice, quant gols
            print(f'   No jogo {i+1} fez {g} gols.')
print('_-' * 20)

