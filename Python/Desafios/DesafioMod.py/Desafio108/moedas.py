def aumentar(preço = 0, taxa = 0, formato=False):
    res= preço + (preço * taxa / 100)
    return res if not formato else moeda


def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if not formato else moeda


def dobro(preço = 0, taxa = 0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço = 0, taxa = 0, formato=False):
    res = preço / 2
    return res if not formato else moeda


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')