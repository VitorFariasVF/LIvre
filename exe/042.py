a = float(input('1º Seguimento: '))
b = float(input('2º Seguimento: '))
c = float(input('3º Sehuimrnto: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    if a == b and b == c:
        print('Triângulo equilátero!')
    elif a == b != c or b == c != a or a == c != b:
        print('Triângulo isósceles!')
    elif a != b != c != a:
        print('Triângulo escaleno')
else:
    print('Não forma triangulo!')
