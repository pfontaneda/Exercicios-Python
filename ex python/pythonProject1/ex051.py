primeiro = int(input('Diga o primeiro termo:'))
razao = int(input('Agora diga a razão:'))
decimo = primeiro + (10 -1) * razao
for PA in range(primeiro, decimo + razao, razao):
    print(PA, end=' - ')
print('FIM')
