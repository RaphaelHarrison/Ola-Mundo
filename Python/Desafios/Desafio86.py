coluna1 = []
coluna2 = []
coluna3 = []
for c1 in range(0,3):
    coluna1.append(int(input('Digite 3 números para a primeira linha da matriz.\nNúmeros: ')))
for c2 in range(0,3):
    coluna2.append(int(input('Digite 3 números para a segunda linha da matriz.\nNúmeros: ')))
for c3 in range(0,3):
    coluna3.append(int(input('Digite 3 números para a terceira linha da matriz.\nNúmeros: ')))

print(f'[{coluna1[0]}][{coluna1[1]}][{coluna1[2]}]')
print(f'[{coluna2[0]}][{coluna2[1]}][{coluna2[2]}]')
print(f'[{coluna3[0]}][{coluna3[1]}][{coluna3[2]}]')