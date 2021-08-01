print('{:*^25}'.format(' Locadoura '))  # aula 07
km = float(input('Kilometros: '))
d = int(input('Dias: '))
ckm = (km*0.15)
cd = (d*60)
ct = cd+ckm
print('{:_^25}'.format(' Recibo '))
print('{:^25}'.format(' Custo por Km: '))
print('{:.>25}'.format(ckm))
print('{:.^25}'.format(' Custo por dia: '))
print('{:.>25}'.format(cd))
print('{:.^25}'.format(' Custo Final! '))
print('RS${:.>22.02f}'.format(ct))
