print('==' * 25)
print('EXERCÍCIO 43!')
print('==' * 25)
n1 = int(input('DIGITE UM PRIMEIRO VALOR: '))
print('==' * 25)
n2 = int(input('DIGITE UM SEGUNDO VALOR: '))
print('==' * 25)

while n2 == 0:
    print('NÃO PODE SER VALOR 0, POR FAVOR ESCOLHA OUTRO NÚMERO!')
    print('==' * 25)
    n2 = int(input('DIGITE UM SEGUNDO VALOR: '))

divisao = n1/n2

print(f'A DIVISÃO DESSES NÚMEROS FOI: {divisao}')
