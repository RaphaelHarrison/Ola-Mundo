valores = []
for cont in range(1,6):
    valores.append(int(input('Digite um número: ')))
m = max(valores)
pm = valores.index(m)
mn = min(valores)
pmn = valores.index(mn)
print(f'A lista é {valores}')
print(f'O maior valor digitado é {max(valores)} e ele está na posição: ', end='')
for i, v in enumerate(valores):
    if v == m:
        print(f'|{i}|', end='')
print(f'\nO menor valor digitado é {min(valores)} e ele está na posição: ', end='')
for i, v in enumerate(valores):
    if v == mn:
        print(f'|{i}|', end='')