from random import randint
pc = randint(0, 5)
print('Pensei em um numero, tente advinhar!')
r = int(input(':'))
if pc == r:
    print('Acertou!')
else:
    print('Errou!')
    print('Pensei numero: {}'.format(pc))
