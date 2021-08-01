#Cores no terminal!
...
#ex \033[:::m  ('\033[:::m') cod para entrada da cor
#STYLE None[0] Bold[1] Underline[4] Negative[7]
#           Text            \          Fundo
#Branco        30           \           40
#Vermelho      31           \           41
#Verde         32           \           42
#Amarelo       33           \           43
#Azul          34           \           44
#Roxo          35           \           45
#Ciano         36           \           46
#Cinza         37           \           47
#print('\033[0:30:41m teste \033[m')
#print('\033[4:33:44m teste \033[m')
#print('\033[0:35:43m teste \033[m')
#print('\033[0:30:42m teste \033[m')
#print('\033[m teste \033[m')
#print('\033[7:30m teste \033[m')
...
#print('\033[31:43:1mOlá, Mundo!\033[m')
#print('\033[4:30:45mOlá, Mundo!\033[m')
#print('\033[30:7mOlá, Mundo!\033[m')
#print('\033[30mOlá, Mundo!\033[m')
#print('\033[33:44mOlá, Mundo!\033[m')
#print('\033[33:7;44mOlá, Mundo!\033[m')
...
#a = 2
#b = 6
#print('Os valores são \033[7;31;40m{}\033[m e \033[7;36;40m{}\033[m'.format(a, b))
...
nome = 'João Vitor'
cor = {'linpo':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pb':'\033[7:30m'}
print('Olá! Muito prazer em te conhecer,{}{}{}\033[m!!!'.format(cor['pb'], nome, cor['linpo']))
print('Olá! Muito prazer em te conhecer,{}{}{}!!!\033[m'.format(cor['pb'], nome, cor['amarelo']))








