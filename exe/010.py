msg = str('Canbio')
print('{:$^22}'.format(msg))   # aula 07
print(f'{msg:§^22}')
rs = float(input('Digite quantos reais:'))
c = 3.27
dl = rs/c
print('Sabendo que o dolar atual vale: R$ {} \nSeu saldo em dolares será {:.2f} $'.format(c, dl))
