print('Gerador de PA(Progressão Aritmética)')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo} → ', end='')
    termo += razão
    c += 1
print('Fim')