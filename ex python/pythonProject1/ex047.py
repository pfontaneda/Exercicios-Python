for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ') #esse end é pra ficar tudo na mesma linha
print('Acabou')
#ou funciona também assim:
for c in range(2, 51, 2):
    print(c, end=' ')
print('Acabou')
