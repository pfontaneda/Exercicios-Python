totI = totH = totM = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu gênero [M/F] ? ')).strip().upper()[0]
    if idade >= 18:
        totI += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ?')).strip().upper()[0]
    print('--' * 20)
    if resp == 'N':
        break
print(f'Temos {totI} pessoas com mais de 18 anos')
print(f'{totH} homens foram cadastrados')
print(f'e {totM} mulheres com menos de 20 anos ')
