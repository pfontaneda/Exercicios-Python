from random import randint
num = (randint(1,10),randint(1,10), randint(1,10),
       randint(1,10), randint(1,10))
print(f'Os valores sorteados foram : {num}')
print(f'O maior número foi: {max(num)}')
print(f'O menor número foi: {min(num)}')

