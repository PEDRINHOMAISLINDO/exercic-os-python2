# 20) Ler dois valores
# (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

print('==' * 25)
print('VALORES DE ORDEM CRESCENTE: ')
print('==' * 25)
n1 = float(input('DIGITE UM NÚMERO: '))
print('==' * 25)
n2 = float(input('DIGITE OUTRO NÚMERO: '))
print('==' * 25)
while n1 == n2:
    print('POR FAVOR, NÃO REPITA OS MESMOS NÚMEROS!!!')
    print('PREENCHA A TABELA NOVAMENTE: ')
    print('==' * 25)
    n1 = float(input('DIGITE UM NÚMERO: '))
    print('==' * 25)
    n2 = float(input('DIGITE OUTRO NÚMERO: '))
    print('==' * 25)
if n1 < n2:
    calculo = n2 - n1
    print(f'SUA ORDEM VAI FICAR {n1:.1f}, {n2:.1f}, {n2 + calculo * 1:.1f}, {n2 + calculo * 2:.1f}, {n2 + calculo * 3:.1f}')
else:
    calculo = n1 - n2
    print(f'SUA ORDEM VAI FICAR {n2:.1f}, {n1:.1f}, {n1 + calculo * 1:.1f}, {n1 + calculo * 2:.1f}, {n1 + calculo * 3:.1f}')
exit()


