from colorama import init, Fore # BIBLIOTECA PARA MUDAR AS CORES DAS LETRAS
init()# SERIA PARA INICIAR O PROGRAMA COLORAMA.

print('=-' * 25) # MULTIPLICANDO A STR "=-" POR 25.
n1 = float(input('DIGITE UM NÚMERO: '))
print('=-' * 25)
n2 = float(input('DIGITE UM SEGUNDO NÚMERO: '))
print('=-' * 25)
n3 = float(input('DIGITE UM TERCEIRO NÚMERO: '))
print('=-' * 25)

while n1 == n2 and n2 == n3: # ESTRUTURA DE REPETIÇÃO PARA IMPEDIR QUE TODOS OS NÚMEROS SEJAM IGUAIS.
    print(Fore.LIGHTRED_EX + 'NÃO DIGITE NÚMEROS IGUAIS!')# Fore.LIGHTRED_EX SERIA UMA FORMA DE ATRIBUIR UMA COR A UMA STR .
    n1 = float(input('DIGITE UM NÚMERO: '))
    print('=-' * 25)
    n2 = float(input('DIGITE UM SEGUNDO NÚMERO: '))
    print('=-' * 25)
    n3 = float(input('DIGITE UM TERCEIRO NÚMERO: '))
    print('=-' * 25)

print(max(n1, n2, n3))# PARA VERIFICAR QUAL É O MAIOR ENTRE n1, n2, n3.
print('=-' * 25)
exit()
