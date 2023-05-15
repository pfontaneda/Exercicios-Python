aluno = {}
aluno['nome'] = str(input('nome: '))
aluno['media'] = float(input('média: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] <7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('_-' * 20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
