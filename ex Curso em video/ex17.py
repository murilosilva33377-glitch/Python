import math
from math import hypot
o=float(input('Qual o valor do cateto oposto:'))
a=float(input('Qual o valor do cateto adjacente:'))
h=math.hypot( o,a)
print(f'O valor da hipotenusa vai medir {(h):.2f}')
