n = str(input('Nome completo:')).title()    # aula 9
nome = n.split()
print('Primeiro nome:{}'.format(nome[0]))
print('Ultimo nome:{}'.format(nome[len(nome)-1]))
