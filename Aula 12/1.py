...#Condições aninhadas
# estrutura IF'Se' Else 'SENAO' Elif 'Senao se '
#ex
# if carro.equerda():
#    carrp.siga()
#    carro.direita()
#    carro.siga()
#    carrp.siga()
#    carro.direita()
#    carro.siga()
#elif carro,siga():
#     carrp.direita()
#     carro.direita()
#     carro.siga()
# else:
#     carro.siga()
# carro.para:
t = '12'
print('\033[7:30m{:=^6}\033[m'.format(t))
nome = str(input('Qual e seu nome? ')).title().strip()
if nome == 'João'or nome == 'Joao':
    print('\033[1:35mQue nome lindo!')
elif nome == 'Clara':
    print('\033[1:31mBelo nome feminino!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Arthur':
    print('\033[1:36mSeu nome até que e bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, \033[1:36m{}!'.format(nome))
