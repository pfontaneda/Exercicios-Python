import emoji
from time import sleep
for c in range(10 , -1, -1): #sempre colocar 1 número a mais pq o laço ignora o último número
    print(c)
    sleep(1)
print('Feliz Ano Novo!')
print(emoji.emojize(':tada:' * 10, language='alias'))
