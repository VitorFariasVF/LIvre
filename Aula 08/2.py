import math
nun = int(input('Digite um número:'))
raiz = math.sqrt(nun)
print('Raiz de {} e igual a {}'.format(nun, raiz))
print('Raiz de {} e igual a {}'.format(nun, math.ceil(raiz)))
print('Raiz de {} e igual a {}'.format(nun, math.floor(raiz)))
print('Raiz de {} e igual a {:.2f}'.format(nun, raiz))
...
from math import sqrt, ceil, floor
nun = int(input('Digite um número:'))
raiz = sqrt(nun)
print('Raiz de {} e igual a {}'.format(nun, raiz))
print('Raiz de {} e igual a {}'.format(nun, ceil(raiz)))
print('Raiz de {} e igual a {}'.format(nun, floor(raiz)))
print('Raiz de {} e igual a {:.2f}'.format(nun, raiz))
