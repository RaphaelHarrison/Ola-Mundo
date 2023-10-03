while True:
    print('=' * 20, 'Tabuada', '=' * 20)
    num = int(input('Entre com um número: '))
    if num < 0:
        break
    for conta in range(1, 11):
        print(f'{num} x {conta} = {num*conta}')
print('='*10, 'Programa Tabuada encerrado', '='*10)