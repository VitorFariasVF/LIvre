cor ={'1':'\033[m',#LINPO
      '2':'\033[7;30m',#PretoBranco
      '3':'\033[7;31;40m',#VermelhoC/Branco
      '4':'\033[31m',#Vermelho
      '5':'\033[33m',#Amarelo
      '6':'\033[36m',#Azul
      '7':'\033[1;33;46m'#AzulAmarelo
      }
print('{} I M C {}'.format(cor['7'], cor['1']))
p = float(input('Peso (KG): '))
a = float(input('Altura (M): '))
imc = p/(a ** 2)
if imc < 18.5:
    print('I M C {} {:.1f} {} \nAbaixo do peso!'.format(cor['4'], imc, cor['1']))
elif 18.5 <= imc < 25:
    print('I M C {} {:.1f} {} \nPeso normal!'.format(cor['6'], imc, cor['1']))
elif 25 <= imc < 30:
    print('I M C {} {:.1f} {} \nSobrepeso!'.format(cor['5'], imc, cor['1']))
elif 30 <= imc < 40:
    print('I M C {} {:.1f} {} \nObesidade!'.format(cor['4'], imc, cor['1']))
elif imc >= 40:
    print('I M C {} {:.1f} {} \nObesidade morbida!'.format(cor['3'], imc, cor['1']))