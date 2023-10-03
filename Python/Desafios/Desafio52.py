num = int(input('Digite um número: '))
tot = 0
c = int
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m',end='')
    else:
        print('\033[31m',end='')
    print(c)
print(f'O número {num} é divisivel por: 1 e {c}')