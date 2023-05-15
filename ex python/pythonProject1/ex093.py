jogador = {}
gols = []
jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    gols.append(int(input(f'   Quantos gols na {c +1}o partida? ')))
jogador['totgol'] = gols[:]
jogador['total'] = sum(gols)
print('_-' * 20)
print(jogador)
print('_-' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('_-' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["totgol"])} partidas')
for i, v in enumerate(jogador['totgol']):
    print(f'   => na partida {i +1}, fez {v} gols')
print(f' Totalizando {jogador["total"]} gols no campeonato')


