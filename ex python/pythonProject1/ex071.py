saque = int(input('Qual o valor do saque? R$ '))
total = saque
nota = 50
totnota = 0
while True:
    if total >= nota:
        total -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f'Total de {totnota} notas de R$ {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnota = 0
        if total == 0:
            break
