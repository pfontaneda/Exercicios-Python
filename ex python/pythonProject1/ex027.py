nome = str(input('Digite seu nome completo:')).strip()
nomec = nome.split()
print('Seu primeiro nome é: {}'.format(nomec[0]))
print('E seu último nome é: {}'.format(nomec[len(nomec)-1]))
