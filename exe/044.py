c ={'1':'\033[m',#LINPO
      '2':'\033[7;30m',#PretoBranco
      '3':'\033[7;31;40m',#VermelhoC/Branco
      '4':'\033[31m',#Vermelho
      '5':'\033[33m',#Amarelo
      '6':'\033[36m',#Azul
      '7':'\033[33;46m'#AzulAmarelo
    }
print('{} ---------------------- {}\n'
      '{}  POV1 Certer Loja 01   {}\n'
      '{} ______________________ {}'
      .format(c['7'], c['1'],c['7'], c['1'],c['7'], c['1']))
p = float(input('Valor da compra:\n'))
f = int(input('Selecione a forma de pagamento:'
              '\n[ 0 ] À vista Dinheiro/Cheque.'
              '\n[ 1 ] Debito.'
              '\n[ 2 ] 1/2x no cartão.'
              '\n[ 3 ] 3x ou mais no cartão\n: '))

if f == 0:
    print('Valor Final [R$]:{:.2f}'.format(p*0.9))
elif f == 1:
    print('Valor Final [R$]:{:.2f}'.format(p*0.95))
elif f == 2:
    print('Valor Final [R$]:{:.2f}'.format(p))
elif f == 3:
    print('Valor Final [R$]:{:.2f}'.format(p*1.2))

