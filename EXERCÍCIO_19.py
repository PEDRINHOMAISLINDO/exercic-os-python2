#19) Ler dois valores
# (considere que não serão lidos valores iguais) e escrever o maior deles.

print('=+' * 25)
print('QUAL É O MAIOR')
print('=+' * 25)
n1 = float(input('DIGITE UM VALOR: '))
print('=+' * 25)
n2 = float(input('DIGITE OUTRO VALOR: '))
print('=+' * 25)
while n1 == n2:
    print('POR FAVOR!, NÃO COLOQUE VALORES IGUAIS!!')
    print('FAÇA NOVAMENTE')
    print('=+' * 25)
    n1 = float(input('DIGITE UM VALOR: '))
    print('=+' * 25)
    n2 = float(input('DIGITE OUTRO VALOR: '))
if n1 > n2:
    print(f'O VALOR {n1} É MAIOR QUE {n2}')
else:
    print(f'O VALOR {n2} É MAIOR QUE {n1}')
exit()

