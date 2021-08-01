cor ={'1':'\033[m',#LINPO
      '2':'\033[7;30m',#PretoBranco
      '3':'\033[7;31;40m',#VermelhoC/Branco
      '4':'\033[31m',#Vermelho
      '5':'\033[33m',#Amarelo
      '6':'\033[36m',#Azul
      '7':'\033[1;33;46m'#AzulAmarelo
        }
t1 = '\033[7;30m#Conversor de sistema numerico!#\033[m'
print(t1)
num = int(input('Digite um nume em decimal: '))
t2 = 'Escolha uma das opções a baixo:\n'\
    '[ 1 ] Binário\n' \
    '[ 2 ] Octal\n' \
    '[ 3 ] Hexadecimal\n'
o = int(input('{}'.format(t2)))
if o == 1 :
    print('Você selecionou a opção:\n'
          '[ 1 ] Binário\n'
          'Valor será: {}{}{}'.format(cor['6'], bin(num), cor['1']))
elif o == 2:
    print('Você selecionou a opção:\n'
          '[ 2 ] Octal\n'
          'Valor será: {}{}{}'.format(cor['6'], oct(num), cor['1']))
elif o == 3:
    print('Você selecionou a opção:\n'
          '[ 3 ] Hexadecimal\n'
          'Valor será: {}{}{}'.format(cor['6'], hex(num), cor['1']))
