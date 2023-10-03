nome = input('Qual é o nome do atleta?')
y = int(input('Ano de nascimento?'))
x = 2023 - y
if x <= 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    print(f'{nome} está na categoria mirim.')
elif x <=10 or 11 or 12 or 13 or 14:
    print(f'{nome} está na categoria infantil.')
elif x <=15 or 16 or 17 or 18 or 19:
    print(f'{nome} está na categoria junior.')
elif x == 20:
    print(f'{nome} está na categoria sênior.')
elif x > 20:
    print(f'{nome} está na categoria master.')
