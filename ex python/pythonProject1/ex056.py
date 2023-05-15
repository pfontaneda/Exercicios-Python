totidade = 0
idhomemvelho = 0
homemvelho = ''
totmulher = 0
for p in range(1, 5):
    print('-------{}º pessoa -------'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    genero = str(input('Gênero (M/F) :')).strip().upper()
    totidade += idade
    if p == 1 and genero == 'M':
        idhomemvelho = idade
        homemvelho = nome
    if genero in 'M' and idade >idhomemvelho:
        idhomemvelho = idade
        homemvelho = nome
    if genero in 'F' and idade < 20:
        totmulher += 1
print("A média de idade é de {:.2f} anos".format(totidade / 4))
print('{} é o homem mais velho'.format(nome))
print('{} mulheres tem menos de 20 anos'.format(totmulher))
