import random
from time import sleep
print('Vamos jogar pedra, papel ou tesoura. Tente ganhar de mim.')
pedra = 1
papel = 2
tesoura = 3
x = input('Escolhe o seu:\n1-Pedra\n2-Papel\n3-Tesoura\nFaça sua escolha: ')
lista = [pedra, papel, tesoura]
escolhido = random.choice(lista)
if x == '1' and escolhido == 1:
    print('Você e eu escolhemos pedra, logo empatamos')
elif x == '1' and escolhido == 2:
    print('Você escolheu pedra e eu escolhi papel, você perdeu.')
elif x == '1' and escolhido == 3:
    print('Você escolheu pedra e eu tesoura, você venceu.')
elif x == '2' and escolhido == 1:
    print('Você escolheu papel e eu escolhi pedra, você venceu.')
elif x == '2' and escolhido == 2:
    print('Eu e você escolhemos papel, logo empatamos.')
elif x == '2' and escolhido == 3:
    print('Você escolheu papel e eu escolhi tesoura, você perdeu.')
elif x == '3' and escolhido == 1:
    print('Você escolheu tesoura e eu escolhi pedra, você perdeu.')
elif x == '3' and escolhido == 2:
    print('Você escolheu tesoura e eu escolhi papel, você ganhou.')
elif x == '3' and escolhido == 3:
    print('Você escolheu tesoura e eu escolhi tesoura. logo empatamos.')