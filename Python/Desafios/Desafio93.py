jogador = {}
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?\nQuantidade: '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}?\nQuantidade: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
for i, v in enumerate(jogador['gols']):
    print(f' =>Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')