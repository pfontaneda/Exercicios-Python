from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastrogeral.txt'

if not arqOk(arq):
    criarArquivo(arq)

cabecalho('SISTEMA ARQUIVO')
while True:
    resposta = menu(['Ver cadastro', 'Novo cadastro', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Sistema finalizado com sucesso. ')
        break
    else:
        print('\033[0;31mERRO! DIGITE UMA OPÇÃO VÁLIDA\033[m')
    sleep(2)
