import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=8jAykqxIeqw&t=147s')
except:
    print('O site não está acessivel no momento')
else:
    print('Consegui acessar o site com sucesso!!')