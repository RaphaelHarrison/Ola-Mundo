temp = []
pr = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pr) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
    pr.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar?[S/N]\nEscolha: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pr)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in pr:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in pr:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
