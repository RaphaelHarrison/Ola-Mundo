from math import hypot
a = float(input('digite o cateto adjacente:'))
o = float(input('digite o cateto oposto:'))
hip = hypot(a,o)
print(f'A hipotenusa é {hip:.2f}')