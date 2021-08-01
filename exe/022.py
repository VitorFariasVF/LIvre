n = str(input('Digite seu nome: ')).strip()   # aula 09
print('Seu nome em maiusculo: {}'.format(n.upper()))
print('Seu nome em minusculo: {}'.format(n.lower()))
print('Qauantidade de letras do seu nome: {} letras.'.format(n.find(' ')))
print('Seu nome Primeno nome tem: {} letras.'.format(len(n)-n.count(' ')))
