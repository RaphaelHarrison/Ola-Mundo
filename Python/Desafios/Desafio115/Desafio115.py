from cev115lib import *
from Desafio115 import arquivo115
from time import sleep

arquivo115 = 'arquivodesafio.txt'

if arquivo115.arquivoExiste



while True:
    resposta = cev115lib.menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        cev115lib.cabeçalho('Opção 1')
    elif resposta == 2:
        cev115lib.cabeçalho('Opção 2')
    elif resposta == 3:
        cev115lib.cabeçalho('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida.\033[m')
    sleep(2)