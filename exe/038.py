c ={'1':'\033[m',#LINPO
      '2':'\033[7;30m',#PretoBranco
      '3':'\033[7;31;40m',#VermelhoC/Branco
      '4':'\033[31m',#Vermelho
      '5':'\033[33m',#Amarelo
      '6':'\033[36m',#Azul
      '7':'\033[33;46m'#AzulAmarelo
        }
t1 = '<<<  Comparador  >>>'
print('{}{}{}'.format(c['3'], t1, c['1']))
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
if n1 > n2:
    print('{}{}{} é maior do que {}{}{}.'.format
          (c['2'], n1, c['1'], c['2'], n2, c['1']))
elif n1 < n2:
    print('{}{}{} é maior do que {}{}{}.'.format
          (c['2'], n2, c['1'], c['2'], n1, c['1']))
elif n1 == n2:
    print('{}{}{} é igual á {}{}{}.'.format
          (c['2'], n1, c['1'], c['2'], n2, c['1']))
