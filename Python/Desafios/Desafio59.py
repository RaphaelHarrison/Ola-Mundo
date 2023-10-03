r = ''
r = str(input('Deseja iniciar a calculadora?[S/N]\nInforme: ')).upper()
while r == 'S':
    r = ''
    d = int(input('Qual função você deseja realizar?\n[1]Somar\n[2]Subtrair\n[3]Multiplicar\n[4]Dividir\n[5]Sair da Calculadora\nInforme: '))

    if d == 1:
        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        s = x + y
        print(f'A soma é {s}')
        r = str(input('Deseja voltar ao menu?[S/N]\nInforme: ')).upper()
        if r == 'N':
            print('Acabou')
    if d == 2:
        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        s = x - y
        print(f'A subtração é {s}')
        r = str(input('Deseja voltar ao menu?[S/N]\nInforme: ')).upper()
        if r == 'N':
            print('Acabou')
    if d == 3:
        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        s = x * y
        print(f'A multiplicação é {s}')
        r = str(input('Deseja voltar ao menu?[S/N]\nInforme: ')).upper()
        if r == 'N':
            print('Acabou')
    if d == 4:
        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        s = x / y
        print(f'A divisão é {s}')
        r = str(input('Deseja voltar ao menu?[S/N]\nInforme: ')).upper()
        if r == 'N':
            print('Acabou')
    if d == 5:
        print('Calculadora desligada.')