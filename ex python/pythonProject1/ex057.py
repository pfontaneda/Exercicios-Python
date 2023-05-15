sexo = str(input('Digite seu gênero [M/F]: ')).strip().upper()[0] #[]pega a letra q quer. no caso a primeira
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, digite de novo por favor: ')).strip().upper()[0]
print('O gênero {} informado é válido'.format(sexo))
