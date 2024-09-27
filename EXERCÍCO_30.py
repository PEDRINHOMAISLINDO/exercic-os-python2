from random import shuffle
print('01' * 25)
print('ORDEM CRESCENTE')
print('01' * 25)
n1 = int(input('DIGITE UM PRIMEIRO NÚMERO: '))
print('01' * 25)
n2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
print('01' * 25)
n3 = int(input('DIGITE O TERCEIRO NÚMERO: '))
print('01' * 25)
lista = [n1, n2, n3]
shuffle(lista)
print(lista)