print('<>' * 25)
print('IGUAIS, PRIMEIRO OU SEGUNDO MAIOR')
print('<>' * 25)
n1 = int(input('DIGITE UM PRIMEIRO NÚMERO: '))
print('<>' * 25)
n2 = int(input('DIGITE UM SEGUNDO NÚMERO: '))
print('<>' * 25)
if n1 == n2:
    print('<>' * 25)
    print(f'O PRIMEIRO E SEGUNDO NÚMERO {n1} E {n2} SÃO NÚMEROS IGUAIS: ')
elif n1 > n2:
    print('<>' * 25)
    print(f'O PRIMEIRO NÚMERO({n1}) É MAIOR QUE ({n2})')
elif n2 > n1:
    print('<>' * 25)
    print(f'O SEGUNDO NÚMERO ({n2}) É MAIOR QUE ({n1})')
exit()
