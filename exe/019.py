from random import choice  # aula 08 sorteio de aluno
n1 = input('Digite os nomes dos alunos: \n')
n2 = input()
n3 = input()
n4 = input()
n5 = input()
List = [n1, n2, n3, n4, n5]
print('Selecionado!\n{}'.format(choice(List)))
