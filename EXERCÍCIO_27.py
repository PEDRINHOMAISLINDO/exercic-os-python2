print('=-' * 25) # MULTIPLICANDO A STR "=-" POR 25
n1 = int(input('DIGITE UM NÚMERO: '))
print('=-' * 25)

if n1 > 0: # ESTRUTURA DE CONDIÇÃO, PARA VERIFICAR O QUE ACONTECE SE O NÚMERO(n1) FOR MAIOR, MENOR OU IGUAL A 0.
    print('NUMERO POSITIVO')
    print('=-' * 25)

elif n1 == 0:
    print('NÚMERO NULO')
    print('=-' * 25)

else:
    print('NÚMERO NEGATIVO')
    print('=-' * 25)

exit() # ENCERRAMENTO DO PROGRAMA.