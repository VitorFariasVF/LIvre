num = int(input('Digite um numero de 0 a 9999 :\n'))    # aula 9
n = str(num)
print('Unidade:{}'.format(n[0]))
print('Dezena:{}'.format(n[1]))
print('Centena:{}'.format(n[2]))
print('Mulhar:{}'.format(n[3]))
print('\n')
n1 = num // 10 % 10
n2 = num // 100 % 10
n3 = num // 1000 % 10
n4 = num // 10000 % 10
print('Unidade:{}'.format(n1))
print('Dezena:{}'.format(n2))
print('Centena:{}'.format(n3))
print('Mulhar:{}'.format(n4))
