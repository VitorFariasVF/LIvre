t = str('TABOADA')   # aula 07
n = int(input('Digite um numero:'))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
# noinspection PyStringFormat
print(f'{t:=^13}')  # print('{:=^13}'.format(t)) # forma aintiga!!!!!!
print('{} * 1 = {}\n{} * 2 = {}\n{} * 3 = {}'.format(n, n1, n, n2, n, n3))
print('{} * 4 = {}\n{} * 5 = {}\n{} * 6 = {}'.format(n, n4, n, n5, n, n6))
print('{} * 7 = {}\n{} * 8 = {}\n{} * 9 = {}'.format(n, n7, n, n8, n, n9))
print('{} * 10 = {}'.format(n, n10))
print(f'{"FIM":=^13}')
