v = int(input('Digite a distancia:'))
if v >= 201:
    c = v*0.45
    print('Sua viagem acima de {:.2f}Km custara {:.2f}R$ \n0.45R$ por kilometro '.format(v, c))
else:
    c = v*0.5
    print('Sua viagem acima de {:.2f}Km custara {:.2f}R$ \n0.5R$ por kilometro '.format(v, c))
