from random import shuffle  # aula 08 Disposição de lista
n1 = input('Digite os nomes dos alunos para a apresentação: \n')
n2 = input()
n3 = input()
n4 = input()
n5 = input()
List = [n1, n2, n3, n4, n5]
shuffle(List)
print('Lista de apresentação!\n{}'.format(List))
