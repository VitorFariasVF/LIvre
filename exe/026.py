f = str(input('Frase:')).strip()    # aula 9
n = f.lower()
print('A letra A aparece {} vezes!'.format(n.count('a')))
print('A primeira letra A aparece na posição {}!'.format(n.find('a')+1))
print('A ultima letra A aparece na posição {}!'.format(n.rfind('a')+1))
