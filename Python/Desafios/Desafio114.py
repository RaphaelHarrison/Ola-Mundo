import urllib
import urllib.request

site = urllib.request.urlopen('http://pudim.com.br')
print('Consegui acessar o site Pudim com sucesso!')
