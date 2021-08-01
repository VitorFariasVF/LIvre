import time
t = time.localtime().tm_year
an = int(input('Digite seu ano de nacimento:'))
i = t - an
if i == 18:
    print('Está na hora de se alistar!')
elif i < 18:
    f = 18 - i + t
    print('Não está na hora, sua idade é {}. Ira se alistar em {}.'.format(i, f))
elif i > 18:
    f = t + 18 - i
    print('Já passou da hora, sua idade é {}. Deveria se alistar em {}.'.format(i, f))