import urllib.request

try:
    site = urllib.request.urlopen('http://www.youtube.com.br')
except:
    print('Deu erro')
else:
    print('Tudo ok')
    print(site.read())
