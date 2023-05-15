from random import choice
#alunos = list()
#for a in range(1, 5):
   # alunos.append(str(input('{}º aluno: '.format(a))))
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
list = [n1, n2, n3, n4]
print('O aluno escolhido foi {}'.format(choice(list)))




