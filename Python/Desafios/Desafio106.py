from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m'    # 4 - azul
     '\033[0;30;45m'    # 5 - roxo
     '\033[7;30;'       # 6 - branco
)

def ajuda(com):
    titulo(f'Acessado o manual do comando \'{com}\'', 4)
    print(c[6], end='')
