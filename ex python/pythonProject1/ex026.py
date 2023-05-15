frase = str(input('Digite a frase:')).strip().lower()
print('A letra a aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira vez que a letra a aparece é na posicão {}'.format(frase.find('a')+1))
print('E a última letra a apararece na posição {}'.format(frase.rfind('a')+1))