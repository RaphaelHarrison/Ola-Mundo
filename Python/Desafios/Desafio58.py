import random
computador = random.randint(0,10)
print('Pensei em um número entre 0 e 10.\nSerá que você consegue acertar?')
acertou = False
palp = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?\nInforme: '))
    palp += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente mais uma vez.\nInforme: ')
        elif jogador > computador:
            print('Menos...tente mais uma vez.\nInforme: ')
print(f'Você acertou com {palp} tentativas.')