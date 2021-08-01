cor ={'1':'\033[m',#LINPO
      '2':'\033[7;30m',#PretoBranco
      '3':'\033[7;31;40m',#VermelhoC/Branco
      '4':'\033[31m',#Vermelho
      '5':'\033[33m',#Amarelo
      '6':'\033[36m',#Azul
      '7':'\033[33;46m'#AzulAmarelo
        }
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('Reprovado, media:{}{:.1f}{}'.format(cor['3'], m, cor['1']))
elif 5 >= m > 7:
    print('Recuperação, media:{}{:.1f}{}'.format(cor['4'], m, cor['1']))
elif m >= 7:
    print('Aprovado, media:{}{:.1f}{}'.format(cor['6'], m, cor['1']))
