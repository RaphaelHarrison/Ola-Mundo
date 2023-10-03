#from random import sample
#list = sample(['Raphael', 'Harrison', 'Santos', 'Marcelino', k=4])
#print(f'Vamos fazer o sorteio dos alunos para a apresentação:\n1) {0};\n2) {1};\n3) {2};\n4) {3}.'.format(list[0], list[1], list[2], list[3])))

import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'A ordem escolhida é {lista}')