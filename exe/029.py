km = int(input('Digite a velocidade:'))
if km >= 80:
    multa = 7*(km-80)
    print('Velocidade excedida! Multado em {:.2f}R$'.format(multa))
else:
    print('Dentro de limite de velocidade!')
print('{:=^7}'.format('FIM'))
