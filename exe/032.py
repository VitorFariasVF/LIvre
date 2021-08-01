from datetime import date
ano = int(input('Digite um ano para amalisar: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano BISSEXTO'.format(ano))
else:
    print('O ano {} Não é BISSEXTO'.format(ano))
