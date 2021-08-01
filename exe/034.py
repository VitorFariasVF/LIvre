s = float(input('Digite o salário:'))
sl = float
if s > 1250:
    sl = s * 1.1
else:
    sl = s * 1.15
print('Seu novo salario sera: {:.2f}RS'.format(sl))
