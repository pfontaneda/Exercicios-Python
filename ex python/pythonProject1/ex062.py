primeiro = int(input('Diga o primeiro termo da PA:'))
razao = int(input('Agora diga a razão:'))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{} - '.format(termo), end = '')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos vc quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados'.format(total))
