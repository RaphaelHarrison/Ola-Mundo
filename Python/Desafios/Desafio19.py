#from random import choice
#print('O aluno sorteado é o {}.'
      #.format(choice(['Raphael', 'Harrison', 'Dos', 'Santos'])))
import random
a1 = str(input('Nome do primeiro aluno:'))
a2 = str(input('Nome do segundo aluno:'))
a3 = str(input('Nome do terceiro aluno:'))
a4 = str(input('Nome do quarto aluno:'))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O aluno escolhido é {escolhido}')
