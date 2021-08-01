from random import randint
from time import sleep
#import time
i = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
j = int(input('Sua escolha:\n'
      '[ 0 ] Pedra\n'
      '[ 1 ] Papel\n'
      '[ 2 ] Tesoura\n: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('A "I.A" escolheu {} '.format(i[pc]))
print('Você jogou {}'.format(i[j]))
if pc == 0:
    if j == 0:
        print('Empate!')
    elif j == 1:
        print('Você venceu!')
    elif j == 2:
        print('"I.A" venceu!')
    else:
        print('Jogada invalida!')
elif pc == 1:
    if j == 0:
        print('"I.A" venceu!')
    elif j == 1:
        print('Empate!')
    elif j == 2:
        print('Você venceu!')
    else:
        print('Jogada invalida!')
elif pc == 2:
    if j == 0:
        print('Você venceu!')
    elif j == 1:
        print('"I.A" venceu!')
    elif j == 2:
        print('Empate!!')
    else:
        print('Jogada invalida!')