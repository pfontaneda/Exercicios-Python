teste = []
teste.append('Patrícia')
teste.append(48)
print(teste)
galera = list()
galera.append(teste[:]) # [:] cria uma cópia sem a ligação com a lista anterior
teste[0] = 'Gustavo'
teste[1] = 40
galera.append(teste[:])
print(galera)
galeras = [["Ana", 20], ['Bia', 30], ['Cloe', 40]]
print(galeras)
print(galera[0])
print(galeras[1][0])
for p in galeras:
    print(p)
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos')
turma = []
dados = [] # estrutura intermediária só pra pegar as informações
totmai = totmen = 0
for c in range(0, 4):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    turma.append(dados[:])
    dados.clear()
print(turma)
for p in turma:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')

