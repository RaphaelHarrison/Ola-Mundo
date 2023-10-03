print('Gerador de PA(Progressão Aritmética)')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} → ', end='')
        termo += razão
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?\nInforme:'))
print(f'A progressão mostrou {c} termos.')
