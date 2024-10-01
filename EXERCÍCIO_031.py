print('=-' * 25)
print('SOMA DOS LADOS DE UM TRIÂNGGULO: ')
print('=-' * 25)
lado_a = int(input('DIGITE UM PRIMEIRO NÚMERO: '))
print('=-' * 25)
lado_b = int(input('DIGITE UM SGUNDO LADO'))
print('=-' * 25)
lado_c = int(input('DIGITE UM TERCEIRO LADO'))
 
if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('UM TRIÂNGULO DA PARA SER FEITO!')
    print('=-' * 25)
else:
    print('A SOMA DOS LADOS NÃO DA PARA FORMAR UM TRIÂNGULO')
    print('=-' * 25)

exit()