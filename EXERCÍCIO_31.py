print('x-' * 25)
print('FORMAÇÃO DE TRIÂNGULO')
print('x-' * 25)
lado_a = float(input('ESCOLHA UM NÚMERO: '))
print('x-' * 25)
lado_b = float(input('ESCOLHA UM SEGUNDO NÚMERO: '))
print('x-' * 25)
lado_c = float(input('ESCOLHA UM TERCEIRO NÚMERO: '))
print('x-' * 25)
if lado_a < (lado_b + lado_c) and lado_b < (lado_c + lado_a) and lado_c < (lado_a + lado_b):
    print('DA PARA FORMA UM TRIÂNGULO')
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO')
exit()