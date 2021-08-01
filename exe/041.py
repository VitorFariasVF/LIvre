import time
n = int(input('Data de nascimento do atleta: '))
ano = time.localtime().tm_year
ct = ano - n

print('Categoria/Idade:')
if ct <= 9:
    print('Mirin\n{}'.format(ct))
elif ct <= 14:
    print('Infantil\n{}'.format(ct))
elif ct <= 19:
    print('Junior\n{}'.format(ct))
elif ct <= 25:
    print('Sênior\n{}'.format(ct))
elif ct > 25:
    print('Master\n{}'.format(ct))
