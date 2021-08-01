# Curso em video Python
# 012345678901234567890
# 000000000011111111112
# fatiamento
print(''''' aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento 
de String, Análise com len(), count(), find(), transformações 
com replace(), upper(), lower(), capitalize(), title(), strip(), 
junção com join().\n''')
frase = str('Curso em video Python')
print(frase)
...# Fatiar
print(frase[9])
print(frase[9:13])
# O 13 no print(frase[9:13]) nao e mostrado
# ultimo caractere mostrado sera o 12 nesse caso!
print(frase[9:21])
print(frase[3])
print(frase[3:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
... # Análise
len(frase)
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
... # transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase1 = str('   Aprenda Python  ')
print(frase1.strip())
print(frase1.rstrip())
print(frase1.lstrip())
... # Divião
print(frase.split())
... # Junção
print('-'.join(frase))
print(frase.split('-'.join(frase)))
print('-'.join(frase.split()))
