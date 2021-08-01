#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
a = float(input('1º segmento:'))
b = float(input('2º segmento:'))
c = float(input('3º segmento:'))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Triangulo existe!')
else:
    print('triangulo não existe!')
