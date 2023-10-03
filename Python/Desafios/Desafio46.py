import time
x = input('A queima de fogos está preste a começar.\n1-Sim\n2-Não\nQuer assistir?\nResposta: ')
if x == '1':
    for c in range(10, 0, -1):
        print(c)
        time.sleep(1)
    print('🥳')
elif x == '2':
    print('Você é chato!')