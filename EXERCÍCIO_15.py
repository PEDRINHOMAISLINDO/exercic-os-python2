# 15) Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo).
from time import sleep
print('==' * 25)
print('POSITIVO OU NWGATIVO')
print('==' * 25)
n1 = int(input('ESCOLHA SEU NUMERO: '))
print('==' * 25)
print('PROCESSANDO...')
sleep(2)
if n1 >= 0:
    print('==' * 25)
    print('NUMERO POSITIVO')
    print('==' * 25)
else:
    print('==' * 25)
    print('NUMERO NEGATIVO')
    print('==' * 25)
exit()
