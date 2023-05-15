primeiro = int(input('Diga o primeiro termo da PA:'))
razao = int(input('Agora diga a razão:'))
termo = primeiro
count = 1
while count <= 10:
    print('{} - '.format(termo), end = '')
    termo += razao
    count += 1
print('FIM')
