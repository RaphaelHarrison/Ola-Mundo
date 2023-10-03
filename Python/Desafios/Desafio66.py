cont = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'O contador da {cont} e a soma da {s}')
