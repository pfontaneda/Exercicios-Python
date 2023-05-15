nome = str(input('Qual é o seu nome?')).strip()
if nome == 'Patrícia':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'José':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino')
elif nome in 'Gustavo, Henrique, Luís':
    print('Belo nome masculino')
else:
    print('Seu nome é bem normal')
print ('Tenha um bom dia , {}!'.format(nome))


