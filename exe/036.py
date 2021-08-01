b = 'Bank Of America'
print('\033[7:30:41m{:*^19}\033[m'.format(b))
sal = float(input('Digite seu salario: '))
casa = float(input('Digite o valor da casa: '))
an = int(input('Digite a quantidade de anos em que deseja pacelar:'))
x = an * 12
p = casa / x
print('Para pagar uma casa de R$\033[36m{:.2f}\033[m '
      'em \033[36m{}\033[m ano(s)\nO valor será! \033[36m{}\033[mx de R$\033[36m{:.2f}'
      .format(casa, an, x, p))
if p <= sal * 0.3:
    print('\033[1:40:36mAPRPVADO\033[m')
elif p > sal * 0.3:
    r = 'REPROVADO'
    print('\033[7:31:40m{:*^19}\033[m'.format(r))
    print('A parcela tem que ser de \033[36m{:.2f}\033[m'.format(sal*0.3))
print('Para pagar uma casa de R$\033[36m{:.2f}\033[m'
      ' em \033[36m{}\033[m ano(s)\nO valor será! \033[36m{}\033[mx de R$\033[36m{:.2f}'.format(casa, an, x, p))
